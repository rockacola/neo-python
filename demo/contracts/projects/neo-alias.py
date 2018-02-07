"""
Test Command:
    build ./demo/contracts/projects/neo-alias.py test 0710 05 True False version
    build ./demo/contracts/projects/neo-alias.py test 0710 05 True False get_storage ['addr2_\x01'] # To peek through a key-value pair

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
VERSION = 10
OWNER = b'#\xba\'\x03\xc52c\xe8\xd6\xe5"\xdc2 39\xdc\xd8\xee\xe9'  # script hash for address: AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y
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
            result = do_get_alias(args)
            return result
        elif operation == 'get_alias_score':  # Fetch score value of the specified address of a specified index
            result = do_get_alias_score(args)
            return result
        elif operation == 'get_aliases':    # Fetch all aliases to the specified address # TODO: consider deprecating this to simplify the contract
            # TODO: need to extend this so instead of results in a string array, it should returns an array of array/object with alias name and vote count
            result = do_get_aliases(args)
            return result
        elif operation == 'vote_alias':     # Cast your vote to the specified address of a specified index, and return with current score
            result = do_vote_alias(args)
            return result

        # Stats
        elif operation == 'count_all':      # Count total alias assigned
            result = do_count_all_aliases()
            return result

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

        # Utilities
        elif operation == 'get_storage':
            result = do_get_storage(args)
            return result
        elif operation == 'set_storage':
            result = do_set_storage(args)
            return result

        Log('unknown operation')
        return False

    Log('invalid request')
    return False


# -- Profile operations


def do_version() -> int:
    version = VERSION + 0
    Log('version:')
    Log(version)
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
        return result
    Notify('invalid argument length')
    return False


def do_get_alias(args: list) -> str:
    if len(args) > 1:
        context = GetContext()
        address = args[0]
        index = args[1]  # TODO: validate input
        result = get_alias(context, address, index)
        return result
    Notify('invalid argument length')
    return False


def do_get_alias_score(args: list) -> int:
    if len(args) > 1:
        context = GetContext()
        address = args[0]
        index = args[1]  # TODO: validate input
        score = get_alias_score(context, address, index)
        return score
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


def do_vote_alias(args: list) -> int:
    # TODO: be conscious about vote caster, keep track of vote log and perform ACL check
    if len(args) > 2:
        context = GetContext()
        address = args[0]
        index = args[1]
        point = args[2]
        count = get_alias_count(context, address)
        if (index < 0 or index >= count):  # Validate target index
            Notify('Invalid index value provided')
            return False
        if point != 1 and point != -1:  # Validate vote point value
            Notify('Invalid vote point provided')
            return False
        else:
            result = vote_alias(context, address, index, point)
            return result
    Notify('invalid argument length')
    return False


def do_count_all_aliases() -> number:
    context = GetContext()
    address = 'all'
    result = get_alias_count(context, address)
    return result


def do_get_storage(args: list) -> bytearray:
    Log('do_get_storage triggered.')
    if len(args) > 0:
        context = GetContext()
        key = args[0]
        Log('key:')
        Log(key)
        value = Get(context, key)
        Log('value:')
        Log(value)
        return value
    Notify('invalid argument length')
    return False


def do_set_storage(args: list) -> bytearray:
    Log('do_set_storage triggered.')
    if len(args) > 1:
        context = GetContext()
        key = args[0]
        Log('key:')
        Log(key)
        value = args[1]
        Log('value:')
        Log(value)
        Put(context, key, value)
        return True
    Notify('invalid argument length')
    return False


# -- Concrete methods


def get_alias_count(context, address: str) -> int:
    # TODO: validate address
    Log('get_alias_count triggered.')
    key = prepare_count_key(address)
    Log('key:')
    Log(key)
    value = Get(context, key)
    if value == None:  # Must use ==. use 'is' provides false negative
        Log('oh, value detected to be None.')
        value = 0
    else:
        value = value + 0  # trick value to always be an integer # NOTE: is this even a real hack?
    Log('value:')
    Log(value)
    return value


def set_alias_count(context, address: str, count: int) -> bool:
    key = prepare_count_key(address)
    Put(context, key, count)
    return True


def increment_alias_count(context, address: str, existing_count: int) -> bool:
    new_count = existing_count + 1
    return set_alias_count(context, address, new_count)


def append_alias(context, address: str, new_alias: str) -> bool:
    # TODO: validate address
    # TODO: validate alias
    # TODO: keep count and store in a 'all_*' key
    Log('append_alias triggered.')
    index = get_alias_count(context, address)
    Log('index:')
    Log(index)
    key = prepare_alias_key(address, index)
    Log('key:')
    Log(key)
    Put(context, key, new_alias)
    # Update counter of this address
    new_count = index + 1
    Log('new_count:')
    Log(new_count)
    set_alias_count(context, address, new_count)
    # Keep track of all records
    all_index = get_all_count(context)
    set_all_alias(context, all_index, key)  # Store alias key as value for all records
    increment_all_count(context, all_index)
    return True


def get_alias(context, address: str, index: int) -> str:
    key = prepare_alias_key(address, index)
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


def vote_alias(context, address: str, index: int, point: int) -> int:
    Log('vote_alias triggered.')
    # Get stored score for this alias
    existing_score = get_alias_score(context, address, index)
    Log('existing_score:')
    Log(existing_score)
    # Update value
    new_score = existing_score + point
    Log('new_score:')
    Log(new_score)
    # Store new score
    set_alias_score(context, address, index, new_score)
    return new_score


def get_alias_score(context, address: str, index: int) -> int:
    Log('get_alias_score triggered.')
    key = prepare_score_key(address, index)
    value = Get(context, key)
    if value == None:
        Log('oh, value detected to be None.')
        value = 0
    return value


def set_alias_score(context, address: str, index: int, score: int) -> bool:
    key = prepare_score_key(address, index)
    Put(context, key, score)
    return True


def get_all_count(context) -> int:
    result = get_alias_count(context, 'all')
    return result


def set_all_alias(context, index: int, value: str) -> bool:
    key = prepare_alias_key('all', index)
    Put(context, key, value)
    return True


def increment_all_count(context, existing_count: int) -> bool:
    result = increment_alias_count(context, 'all', existing_count)
    return result


# -- Helper methods


def prepare_count_key(address: str) -> str:
    key = concat(address, '_count')
    return key


def prepare_alias_key(address: str, index: int) -> str:
    key = concat(address, '_')
    key = concat(key, index)
    return key


def prepare_score_key(address: str, index: int) -> str:
    key = concat(address, '_')
    key = concat(key, index)
    key = concat(key, '_score')
    return key
