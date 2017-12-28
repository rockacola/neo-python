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
    import contract ./demo/contracts/AccessControl.avm 07 02 True False

Import Response:
    Test deploy invoke successful
    Total operations executed: 11
    Results ['IOp Interface: <neo.Core.State.ContractState.ContractState object at 0x110974dd8> ']
    Deploy Invoke TX gas cost: 490.0
    Deploy Invoke TX Fee: 0.0

Example Invocation:
    testinvoke 10c5b1f79880b2751ef06d2e0c65d2b2babd0b7a version

Example Response:
    Test invoke successful
    Total operations: 80
    Results ['Integer: 1 ']
    Invoke TX gas cost: 0.0
    Invoke TX Fee: 0.001

More Example Invokes:
    testinvoke 10c5b1f79880b2751ef06d2e0c65d2b2babd0b7a is_owner
"""
from boa.blockchain.vm.Neo.Storage import Get, Put, Delete, GetContext
from boa.blockchain.vm.Neo.Runtime import Log, Notify, GetTrigger, CheckWitness

# Global
OWNER = b'#\xba\'\x03\xc52c\xe8\xd6\xe5"\xdc2 39\xdc\xd8\xee\xe9' # script hash for address: AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y
VERSION = 1

def Main(operation, args):
    """

    :param operation: str The name of the operation to perform
    :param args: list A list of arguments along with the operation
    :return:
        bytearray: The result of the operation
    """
    if operation == 'version':
        return do_version()
    if operation == 'is_owner':
        return do_is_owner()
    return 'unknown operation'

def do_version():
    return VERSION

def do_is_owner():
    return CheckWitness(OWNER)
