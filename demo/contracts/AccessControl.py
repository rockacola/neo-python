"""
ACL Smart Contract

Purpose of this contract is to illustrate user access control.
Where different addresses have the right to perform various set 
of actions depends on assigned privileges.

- contract owner is hardcoded to a predetermined address

"""
"""
Test Command:
    build ./demo/contracts/AccessControl.py test 0710 05 True False version

Test Response:
    Calling ./demo/contracts/AccessControl.py with arguments ['version']
    Test deploy invoke successful
    Used total of 80 operations
    Result b'\x01'
    Invoke TX gas cost: 0.001

Import Command:
    import contract ./demo/contracts/AccessControl.avm 0710 05 True False

Import Response:
    Test deploy invoke successful
    Total operations executed: 11
    Results ['IOp Interface: <neo.Core.State.ContractState.ContractState object at 0x110974dd8> ']
    Deploy Invoke TX gas cost: 490.0
    Deploy Invoke TX Fee: 0.0

Example Invocation:
    testinvoke 4b96787b1a2f7f11cebdf2f3c5cf2899e1a1886a version

Example Response:
    Test invoke successful
    Total operations: 80
    Results ['Integer: 1 ']
    Invoke TX gas cost: 0.0
    Invoke TX Fee: 0.001

More Example Invokes:
    testinvoke 4b96787b1a2f7f11cebdf2f3c5cf2899e1a1886a is_owner
    testinvoke 4b96787b1a2f7f11cebdf2f3c5cf2899e1a1886a get_trigger
    testinvoke 4b96787b1a2f7f11cebdf2f3c5cf2899e1a1886a get_tx
"""
from boa.blockchain.vm.Neo.Storage import Get, Put, Delete, GetContext
from boa.blockchain.vm.Neo.Runtime import Log, Notify, GetTrigger, CheckWitness
from boa.blockchain.vm.Neo.Transaction import GetHash
from boa.blockchain.vm.System.ExecutionEngine import GetScriptContainer

# Global
VERSION = 2
OWNER = b'#\xba\'\x03\xc52c\xe8\xd6\xe5"\xdc2 39\xdc\xd8\xee\xe9' # script hash for address: AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y
# GAS_ASSET_ID = b'\xe7\x2d\x28\x69\x79\xee\x6c\xb1\xb7\xe6\x5d\xfd\xdf\xb2\xe3\x84\x10\x0b\x8d\x14\x8e\x77\x58\xde\x42\xe4\x16\x8b\x71\x79\x2c\x60';

def Main(operation, args):
    """

    :param operation: str The name of the operation to perform
    :param args: list A list of arguments along with the operation
    :return:
        bytearray: The result of the operation
    """
    if operation == 'version':
        return do_version()
    elif operation == 'get_trigger':
        return do_get_trigger()
    elif operation == 'get_tx':
        return do_get_tx()
    elif operation == 'is_owner':
        return do_is_owner()
    return 'unknown operation'

def do_version():
    version = VERSION
    Notify(version)
    return version

def do_get_trigger():
    trigger = GetTrigger()
    return trigger

def do_get_tx():
    """Fetches the hash of the current transaction.

    Return:
        (str): hash of current transaction.
    """
    transaction = GetScriptContainer()
    Log(transaction)
    hash_val = GetHash(transaction)
    return hash_val

def do_is_owner():
    return CheckWitness(OWNER)