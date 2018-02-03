"""
NeoAlias Smart Contract

Give alias to wallet addresses

TODO:
    - Modularise into classes
    - Doc comment
    - Hard cap 10 aliases per address
    - Hard cap 20 characters per alias
    - Use another storage to keep track of alias count
    - Validate input address
    - Validate input alias (with regex)
"""
"""
Test Command:
    build ./demo/contracts/NeoAlias.py test 0710 05 True False version

Import Command:
    import contract ./demo/contracts/NeoAlias.avm 0710 05 True False

Example Invocation:
    testinvoke 4f74c41ce60dcc8abb6f5b396935430f9d3b1db1 version

More Example Invokes:
    testinvoke 4f74c41ce60dcc8abb6f5b396935430f9d3b1db1 get_alias ['AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y']
    testinvoke 4f74c41ce60dcc8abb6f5b396935430f9d3b1db1 set_alias ['AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y','lorem']
"""
from boa.blockchain.vm.Neo.Runtime import Log, Notify, GetTrigger, CheckWitness
from boa.blockchain.vm.Neo.Blockchain import GetHeight, GetHeader
from boa.blockchain.vm.Neo.Action import RegisterAction
from boa.blockchain.vm.Neo.TriggerType import Application, Verification
from boa.blockchain.vm.Neo.Storage import GetContext, Get, Put, Delete
from boa.code.builtins import concat, list, range, take, substr

# Global
VERSION = 5
OWNER = b'#\xba\'\x03\xc52c\xe8\xd6\xe5"\xdc2 39\xdc\xd8\xee\xe9' # script hash for address: AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y
# NEO_ASSET_ID = b'\x9b|\xff\xda\xa6t\xbe\xae\x0f\x93\x0e\xbe`\x85\xaf\x90\x93\xe5\xfeV\xb3J\\"\x0c\xcd\xcfn\xfc3o\xc5'
# GAS_ASSET_ID = b'\xe7-(iy\xeel\xb1\xb7\xe6]\xfd\xdf\xb2\xe3\x84\x10\x0b\x8d\x14\x8ewX\xdeB\xe4\x16\x8bqy,`'

def Main(operation, args):
    """

    :param operation: The name of the operation to perform
    :param args: A list of arguments along with the operation
    :type operation: str
    :type args: list
    :return: The result of the operation
    :rtype: bytearray
    """
    trigger = GetTrigger()

    if trigger == Verification():
        is_owner = CheckWitness(OWNER)
        Log('Check is_owner:')
        Log(is_owner)
        if is_owner:
            return True
        return False

    elif trigger == Application():
        if operation == 'version':
            return do_version()
        elif operation == 'is_owner':
            return do_is_owner()
        elif operation == 'set_alias':
            return do_set_alias(args)
        elif operation == 'get_alias':
            return do_get_alias(args)
        Log('unknown operation')
        return False

    Log('invalid request')
    return False


def do_version():
    version = VERSION
    Notify(version)
    return version


def do_is_owner():
    return CheckWitness(OWNER)


def do_set_alias(args):
    if len(args) > 1:
        context = GetContext()
        address = args[0]
        alias = args[1]
        return set_alias(context, address, alias)
    Notify('invalid argument length')
    return False


def do_get_alias(args):
    if len(args) > 0:
        context = GetContext()
        address = args[0]
        return get_aliases(context, address)
    Notify('invalid argument length')
    return False


def set_alias(context, address, new_alias):
    alias_list_bytes = Get(context, address)
    if not alias_list_bytes:
        Log('no existing aliases to this address')
        alias_list = [new_alias]
        alias_list_bytes = serialize_array(alias_list)
        Put(context, address, alias_list_bytes)
        return True
    else:
        alias_list = deserialize_bytearray(alias_list_bytes)
        alias_list.append(new_alias)
        alias_list_bytes = serialize_array(alias_list)
        Put(context, address, alias_list_bytes)
        return True


def get_aliases(context, address):
    alias_list_bytes = Get(context, address)
    if not alias_list_bytes:
        Log('no designated aliases to this address')
        return ''
    else:
        return deserialize_bytearray(alias_list_bytes)


def deserialize_bytearray(data):

    # ok this is weird.  if you remove this print statement, it stops working :/

    # get length of length
    collection_length_length = data[0:1]

    # get length of collection
    collection_len = data[1:collection_length_length + 1]

    # create a new collection
    new_collection = list(length=collection_len)

    # trim the length data
    offset = 1 + collection_length_length

    for i in range(0, collection_len):

        # get the data length length
        itemlen_len = data[offset:offset + 1]

        # get the length of the data
        item_len = data[offset + 1:offset + 1 + itemlen_len]

        # get the data
        item = data[offset + 1 + itemlen_len: offset + 1 + itemlen_len + item_len]

        # store it in collection
        new_collection[i] = item

        offset = offset + item_len + itemlen_len + 1

    return new_collection


def serialize_array(items):

    # serialize the length of the list
    itemlength = serialize_var_length_item(items)

    output = itemlength

    # now go through and append all your stuff
    for item in items:

        # get the variable length of the item
        # to be serialized
        itemlen = serialize_var_length_item(item)

        # add that indicator
        output = concat(output, itemlen)

        # now add the item
        output = concat(output, item)

    # return the stuff
    return output


def serialize_var_length_item(item):

    # get the length of your stuff
    stuff_len = len(item)

    # now we need to know how many bytes the length of the array
    # will take to store

    # this is one byte
    if stuff_len <= 255:
        byte_len = b'\x01'
    # two byte
    elif stuff_len <= 65535:
        byte_len = b'\x02'
    # hopefully 4 byte
    else:
        byte_len = b'\x04'

    out = concat(byte_len, stuff_len)

    return out
