"""
This is to follow NEP5-like contract structure.
REF: https://medium.com/proof-of-working/how-to-build-an-ico-on-neo-with-the-nex-ico-smart-contract-template-1beac1ff0afd
"""
"""
Test Command:
    build ./demo/contracts/IncrementsPlus.py test 0710 05 True False increase

Test Response:
    Calling ./demo/contracts/IncrementsPlus.py with arguments ['increase']
    Test deploy invoke successful
    Used total of 123 operations
    Result b'\x01'
    Invoke TX gas cost: 0.001

Import Command:
    import contract ./demo/contracts/IncrementsPlus.avm 0710 05 True False

Import Response:
    Test deploy invoke successful
    Total operations executed: 11
    Results ['IOp Interface: <neo.Core.State.ContractState.ContractState object at 0x113dacd68> ']
    Deploy Invoke TX gas cost: 490.0
    Deploy Invoke TX Fee: 0.0

Example Invocation:
    testinvoke 0822b132f1498f49fd3ed90e18934c3c6b1a7a71 show

Example Response:
    Test invoke successful
    Total operations: 91
    Results ['Integer: 0 ']
    Invoke TX gas cost: 0.0
    Invoke TX Fee: 0.001
"""
from boa.blockchain.vm.Neo.Storage import Get, Put, Delete, GetContext
from boa.blockchain.vm.Neo.Runtime import Notify


def Main(operation, args):
    """

    :param operation: str The name of the operation to perform
    :param args: list A list of arguments along with the operation
    :return:
        bytearray: The result of the operation
    """
    context = GetContext()
    currentCount = Get(context, 'counter')

    if operation == 'reset':
        print("reset triggered")
        Put(context, 'counter', 0)
        return 0
    elif operation == 'show':
        print("show triggered")
        currentCount += 0
        return currentCount
    elif operation == 'welcome':
        print("welcome triggered")
        return 'Welcome to Increment2 contract!'
    elif operation == 'increase':
        print("increase triggered")
        currentCount += 1
        Put(context, 'counter', currentCount)
        return currentCount
    elif operation == 'decrease':
        print("decrease triggered")
        currentCount -= 1
        Put(context, 'counter', currentCount)
        return currentCount
    else:
        print("invalid parameter")
        return 'unknown operation'
