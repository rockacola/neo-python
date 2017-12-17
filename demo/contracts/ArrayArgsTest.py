"""
Test Command:
    build ./demo/contracts/ArrayArgsTest.py test 0705 02 True False dostuff 42

Test Response:
    Calling ./demo/contracts/ArrayArgsTest.py with arguments ['dostuff', '42']
    Test deploy invoke successful
    Used total of 74 operations
    Result 23
    Invoke TX gas cost: 0.001

Import Command:
    import contract ./demo/contracts/ArrayArgsTest.avm 0705 02 True False

Import Response:
    Test deploy invoke successful
    Total operations executed: 11
    Results ['IOp Interface: <neo.Core.State.ContractState.ContractState object at 0x105311c50> ']
    Deploy Invoke TX gas cost: 490.0
    Deploy Invoke TX Fee: 0.0

Example Invocation:
    testinvoke 926be598e97b740aa86087d84194caf84e03b006 dostuff 42

Example Response:
    Test invoke successful
    Total operations: 74
    Results ["ByteArray: b'\\x17'"]
    Invoke TX gas cost: 0.0
    Invoke TX Fee: 0.001

"""
from boa.blockchain.vm.Neo.Runtime import Log
from boa.code.builtins import concat


def Main(operation, items):
    """

    :param operation:
    :param items:
    :return:
    """
    j = 10

    if operation == 'dostuff':

        j = 3

        if len(items) == 2:

            bytes1 = items[0]
            bytes2 = items[1]

            len1 = len(bytes1)
            len2 = len(bytes2)

            total = concat(bytes1, bytes2)

#            j = len1 + len2

            if total == 137707327489:
                Log("awesome!")

            else:
                Log("bad")

        else:

            j = 23

    elif operation == 'dont':

        j = 4

    return j
