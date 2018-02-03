"""
Test Command:
    build ./demo/contracts/StorageTest.py test ff 07 True False

Test Response:
    Calling ./demo/contracts/StorageTest.py with arguments []
    Test deploy invoke successful
    Used total of 114 operations
    Result hhhhhhh
    Invoke TX gas cost: 0.001

Import Command:
    import contract ./demo/contracts/StorageTest.avm ff 07 True False

Import Response:
    Test deploy invoke successful
    Total operations executed: 11
    Results ['IOp Interface: <neo.Core.State.ContractState.ContractState object at 0x105b24f98> ']
    Deploy Invoke TX gas cost: 490.0
    Deploy Invoke TX Fee: 0.0

Example Invocation:
    testinvoke 26a5fd352746e7e22a3035651753596a417c165b

Example Response:
    Test invoke successful
    Total operations: 114
    Results ["ByteArray: bytearray(b'hhhhhhh')"]
    Invoke TX gas cost: 0.0
    Invoke TX Fee: 0.001
"""
from boa.blockchain.vm.Neo.Storage import Get, Put, Delete, GetContext
from boa.blockchain.vm.Neo.Runtime import Notify


def Main():
    """

    :return:
    """
    context = GetContext()

    print("hello")
    Notify(context)

    item_key = 'hello'
    item_val = 'hhhhhhh'
    Notify(item_val)
    Put(context, item_key, item_val)
    print("hhhh")
    a = 1

    out = Get(context, item_key)

    return out
