"""
Test Command:
    build ./demo/contracts/projects/neo-alias.py test 0710 05 True False version

Import Command:
    import contract ./demo/contracts/projects/neo-alias.avm 0710 05 True False

Example Invocation:
    testinvoke ff8e5db265676e04262ee0d05c3f02fee97439bc version
"""
from boa.blockchain.vm.System.ExecutionEngine import GetScriptContainer, GetExecutingScriptHash
from boa.blockchain.vm.Neo.Transaction import *
from boa.blockchain.vm.Neo.Runtime import Log, Notify, GetTrigger, CheckWitness
from boa.blockchain.vm.Neo.Blockchain import GetHeight, GetHeader
from boa.blockchain.vm.Neo.Action import RegisterAction
from boa.blockchain.vm.Neo.TriggerType import Application, Verification
from boa.blockchain.vm.Neo.Storage import GetContext, Get, Put, Delete
from boa.blockchain.vm.Neo.Output import GetScriptHash, GetValue, GetAssetId
from boa.code.builtins import concat, list, range, take, substr


# Global
VERSION = 9
OWNER = b'#\xba\'\x03\xc52c\xe8\xd6\xe5"\xdc2 39\xdc\xd8\xee\xe9' # script hash for address: AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y
# NEO_ASSET_ID = b'\x9b|\xff\xda\xa6t\xbe\xae\x0f\x93\x0e\xbe`\x85\xaf\x90\x93\xe5\xfeV\xb3J\\"\x0c\xcd\xcfn\xfc3o\xc5'
# GAS_ASSET_ID = b'\xe7-(iy\xeel\xb1\xb7\xe6]\xfd\xdf\xb2\xe3\x84\x10\x0b\x8d\x14\x8ewX\xdeB\xe4\x16\x8bqy,`'





def Main(operation: str, args: list) -> bytearray:
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
            result = do_version()
            return result
        elif operation == 'is_owner':       # Checking if invoker is the owner of the smart contract
            result = do_is_owner()
            return result

        # Standard
        elif operation == 'count_alias':    # Count numbers of alias assigned to the specified address
            result = do_count_alias(args)
            return result
        elif operation == 'set_alias':      # Append a new alias to the specified address
            result = do_set_alias(args)
            return result
        elif operation == 'get_alias':      # Fetch alias name to the specified address of a specified index
            # TODO: need to extend this so instead of results in a string, it should returns an array/object with alias name and vote count
            result = do_get_alias(args)
            return result
        elif operation == 'get_aliases':
            # TODO: need to extend this so instead of results in a string array, it should returns an array of array/object with alias name and vote count
            result = do_get_aliases(args)
            return result
        # TODO: vote_alias(address: str, point: int)
        # TODO: list_all_aliases()

        # Moderation
        # TODO: mark_bad_address(address, str)
        # TODO: unmark_bad_address(address, str)
        # TODO: mark_bad_alias(address, str, index: int)
        # TODO: unmark_bad_alias(address, str, index: int)

        # Access control
        # TODO: assign_mod(address: str)
        # TODO: resign_mod(address: str)
        # TODO: assign_admin(address: str)
        # TODO: resign_admin(address: str)

        Log('unknown operation')
        return False

    Log('invalid request')
    return False


# -- Profile operations


def do_version() -> int:
    version = VERSION + 0
    Notify(version)
    return version


def do_is_owner() -> bool:
    return CheckWitness(OWNER)


# -- Standard operations


def do_count_alias(args: list) -> int:
    # Log('do_count_alias triggered.')
    # Log('args:')
    # Log(args)
    if len(args) > 0:
        context = GetContext()
        address = args[0]
        result = get_alias_count(context, address)
        return result
    Notify('invalid argument length')
    return False


def do_set_alias(args: list) -> bool:
    if len(args) > 0:
        context = GetContext()
        address = args[0]
        new_alias = args[1]
        result = append_alias(context, address, new_alias)
        # TODO: keep count and store in a 'all_*' key
        return result
    Notify('invalid argument length')
    return False


def do_get_alias(args: list) -> str:
    if len(args) > 1:
        context = GetContext()
        address = args[0]
        index = args[1]
        result = get_alias(context, address, index)
        return result
    Notify('invalid argument length')
    return False


def do_get_aliases(args: list) -> list:
    if len(args) > 0:
        context = GetContext()
        address = args[0]
        result = get_aliases(context, address)
        return result
    Notify('invalid argument length')
    return False


# -- Concrete methods


def get_alias_count(context, address: str) -> int:
    # TODO: validate address
    key = concat(address, '_count')
    value = Get(context, key)
    value += 0  # trick value to always be an integer
    return value


def set_alias_count(context, address: str, count: int) -> bool:
    key = concat(address, '_count')
    Put(context, key, count)
    return True


def append_alias(context, address: str, new_alias: str) -> bool:
    # TODO: validate address
    # TODO: validate alias
    count = get_alias_count(context, address)
    index = count
    key = concat(address, '_')
    key = concat(key, index)    # So you get "{addr}_{index}" as key
    Log('key:')
    Log(key)
    Put(context, key, new_alias)
    new_count = count + 1
    Log('new_count:')
    Log(new_count)
    set_alias_count(context, address, new_count)
    return True


def get_alias(context, address: str, index: int) -> str:
    key = concat(address, '_')
    key = concat(key, index)    # So you get "{addr}_{index}" as key
    alias = Get(context, key)
    Log('alias:')
    Log(alias)
    return alias


def get_aliases(context, address: str) -> list:
    # NOTE: Untested code
    count = get_alias_count(context, address)
    i = 0
    alias_list = []
    while (i < count):
        alias = get_alias(context, address, i)
        alias_list.append(alias)
        i = i + 1
    return alias_list


# -- Helper methods

