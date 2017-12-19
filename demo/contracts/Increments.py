"""
Test Command:
    build ./demo/contracts/Increments.py test 07 02 True False increase

Test Response:
    Calling ./demo/contracts/Increments.py with arguments ['increase']
    Test deploy invoke successful
    Used total of 108 operations
    Result 1
    Invoke TX gas cost: 0.001

Import Command:
    import contract ./demo/contracts/Increments.avm 07 02 True False

Import Response:
    Test deploy invoke successful
    Total operations executed: 11
    Results ['IOp Interface: <neo.Core.State.ContractState.ContractState object at 0x105d42da0> ']
    Deploy Invoke TX gas cost: 490.0
    Deploy Invoke TX Fee: 0.0

Example Invocation:
    testinvoke 5f58f9640b21913eba429417d689413095311430 increase

Example Response:
    Test invoke successful
    Total operations: 108
    Results ['Integer: 1 ']
    Invoke TX gas cost: 0.0
    Invoke TX Fee: 0.001
"""
from boa.blockchain.vm.Neo.Storage import Get, Put, Delete, GetContext
from boa.blockchain.vm.Neo.Runtime import Notify


def Main(operation):
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
    elif operation == 'increase':
        print("increase triggered")
        currentCount += 1
        Put(context, 'counter', currentCount)
        return currentCount
    elif operation == 'decrease':
        print("decrease triggered")
        currentCount -= 1
        Put(context, 'counter', currentCount)
    else:
        print("invalid parameter")
        return -1
