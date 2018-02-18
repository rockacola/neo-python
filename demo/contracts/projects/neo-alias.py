from boa.blockchain.vm.System.ExecutionEngine import GetScriptContainer
from boa.blockchain.vm.Neo.Transaction import *
from boa.blockchain.vm.Neo.Runtime import Log, Notify, GetTrigger, CheckWitness
from boa.blockchain.vm.Neo.Blockchain import GetHeight, GetHeader
from boa.blockchain.vm.Neo.TriggerType import Application, Verification
from boa.blockchain.vm.Neo.Storage import GetContext, Get, Put
from boa.blockchain.vm.Neo.Output import GetScriptHash
from boa.code.builtins import concat, list, range


# Global
VERSION = 17
OWNER = b'\x96P\xac\xd6\xb7S,\xb4\xeaiU\xedK\x0f\xd3\xaa\xa9\xc9Q\x87'  # Script has for AVUfegS354LWRoBuCzuKjGCYkT3tnpFFTD


# -- Chain of command


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
            result = do_get_aliases(args)
            return result
        elif operation == 'vote_alias':     # Cast your vote to the specified address of a specified index, and return with current score
            result = do_vote_alias(args)
            return result

        # Stats
        elif operation == 'count_all':      # Count total alias assigned
            result = do_count_all_aliases()
            return result

        # Admin Utilities
        elif operation == 'get_storage':
            result = do_get_storage(args)
            return result
        elif operation == 'set_storage':
            result = do_set_storage(args)
            return result
        elif operation == 'my_address':
            result = get_invoker_address()
            return result

        Log('unknown operation')
        return False

    Log('invalid request')
    return False


# -- Operation delegator with input validation


def do_version() -> int:
    version = VERSION + 0
    Log('version:')
    Log(version)
    return version


def do_is_owner() -> bool:
    return CheckWitness(OWNER)


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
    if len(args) > 2:
        context = GetContext()
        invoker_address = args[0]
        target_address = args[1]
        new_alias = args[2]
        is_match = CheckWitness(invoker_address)
        # Log('Check is_match:')
        # Log(is_match)
        if is_match == False:  # Validate invoker
            Notify('mismatch invoker address')
            return False
        result = set_alias(context, invoker_address, target_address, new_alias)
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
    if len(args) > 3:
        context = GetContext()
        invoker_address = args[0]
        target_address = args[1]
        index = args[2]
        point = args[3]
        count = get_alias_count(context, target_address)
        if (index < 0 or index >= count):  # Validate target index
            Notify('invalid index value provided')
            return False
        if point != 1 and point != -1:  # Validate vote point value
            Notify('invalid vote point provided')
            return False
        else:
            is_match = CheckWitness(invoker_address)
            # Log('Check is_match:')
            # Log(is_match)
            if is_match == False:  # Validate invoker
                Notify('mismatch invoker address')
                return False
            result = vote_alias(context, invoker_address, target_address, index, point)
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
    is_owner = CheckWitness(OWNER)
    if is_owner == False:
        Notify('permission denied')
        return False
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
    is_owner = CheckWitness(OWNER)
    if is_owner == False:
        Notify('permission denied')
        return False
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


# -- Concrete methods with business logic


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
    is_success = set_alias_count(context, address, new_count)
    return is_success


def set_alias(context, invoker_address: str, target_address: str, new_alias: str) -> bool:
    # TODO: get invokers address
    # TODO: verify if this is the first time invoker assigning alias to target address
    Log('set_alias triggered.')
    index = get_alias_count(context, target_address)
    Log('index:')
    Log(index)
    key = prepare_alias_key(target_address, index)
    Log('key:')
    Log(key)
    Put(context, key, new_alias)
    # Update counter of this address
    new_count = index + 1
    Log('new_count:')
    Log(new_count)
    set_alias_count(context, target_address, new_count)
    # Keep track of all records
    all_index = get_all_count(context)
    Log('all_index:')
    Log(all_index)
    set_all_alias(context, all_index, key)  # Store alias key as value for all records
    increment_all_count(context, all_index)
    # log invoker's address assignment by cast default 1 point vote
    vote_alias(context, invoker_address, target_address, index, 1)  # TODO: we can reduce GAS cost by omit check_has_voted()
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


def vote_alias(context, invoker_address: str, target_address: str, index: int, point: int) -> int:
    Log('vote_alias triggered.')
    # check if already voted previously
    has_voted = check_has_voted(context, invoker_address, target_address, index)
    Log('has_voted:')
    Log(has_voted)
    if has_voted == False:
        # Get stored score for this alias
        existing_score = get_alias_score(context, target_address, index)
        Log('existing_score:')
        Log(existing_score)
        # Update value
        new_score = existing_score + point
        Log('new_score:')
        Log(new_score)
        # Store new score
        set_alias_score(context, target_address, index, new_score)
        # Set vote log
        log_vote(context, invoker_address, target_address, index, new_score)
        return new_score
    else:
        Notify('invoker has already voted for this alias')
        return False


def get_alias_score(context, address: str, index: int) -> int:
    Log('get_alias_score triggered.')
    key = prepare_score_key(address, index)
    value = Get(context, key)
    if value == None:
        Log('existing score value detected to be None.')
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


def check_has_voted(context, invoker_address: str, target_address: str, index: int) -> bool:
    Log('check_has_voted triggered')
    key = prepare_log_vote_key(invoker_address, target_address, index)
    value = Get(context, key)
    Log('value:')
    Log(value)
    if value == None:
        return False
    else:
        return True


def log_vote(context, invoker_address: str, target_address: str, index: int, score: int) -> bool:
    key = prepare_log_vote_key(invoker_address, target_address, index)
    Put(context, key, score)
    return True


# -- Dumb, functional methods


def prepare_count_key(address: str) -> str:
    # Format: {address}_count
    key = concat(address, '_count')
    return key


def prepare_alias_key(address: str, index: int) -> str:
    # Format: {address}_{index}
    key = concat(address, '_')
    key = concat(key, index)
    return key


def prepare_score_key(address: str, index: int) -> str:
    # Format: {address}_{index}_score
    key = concat(address, '_')
    key = concat(key, index)
    key = concat(key, '_score')
    return key


def prepare_log_vote_key(invoker_address: str, target_address: str, index: int) -> str:
    # Format: {target_address}_{alias_index}_{invoker_address}
    key = concat(target_address, '_')
    key = concat(key, index)
    key = concat(key, '_')
    key = concat(key, invoker_address)
    return key


def get_invoker_address() -> str:
    '''
    I don't think you can Log() tx, references nor reference.
    Also you cannot really have validators in place, things like "if tx is not None" error'ed out.
    '''
    Log('get_invoker_address triggered.')
    tx = GetScriptContainer()
    references = tx.References
    reference = references[0]
    sender_addr = reference.ScriptHash
    Log('sender_addr:')
    Log(sender_addr)
    return sender_addr
