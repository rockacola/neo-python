"""
Test Command:
    build ./demo/contracts/Fibonacci.py test 02 02 True False 7

Test Response:
    Calling ./demo/contracts/Fibonacci.py with arguments ['7']
    Test deploy invoke successful
    Used total of 1733 operations
    Result 13
    Invoke TX gas cost: 0.001

Import Command:
    import contract ./demo/contracts/Fibonacci.avm 02 02 True False

Import Response:
    Test deploy invoke successful
    Total operations executed: 11
    Results ['IOp Interface: <neo.Core.State.ContractState.ContractState object at 0x10b19fda0> ']
    Deploy Invoke TX gas cost: 490.0
    Deploy Invoke TX Fee: 0.0

Example Invocation:
    testinvoke 3147293325d465b73a692112f54295718fabd35f 7

Example Response:
    Test invoke successful
    Total operations: 1733
    Results ['Integer: 13 ']
    Invoke TX gas cost: 0.0
    Invoke TX Fee: 0.001

NOTE:
- It's having trouble calculating around 12 and above.
- Eg/ calling fibonacci of 20 takes ~1 minutes to calculate, costs 678.01 GAS

"""
def Main(fibnumber):
    """

    :param fibnumber:
    :return:
    """
    fibresult = fib(fibnumber)

    return fibresult


def fib(n):
    """

    :param n:
    :return:
    """
    if n == 1 or n == 2:
        return 1

    n1 = n - 1
    n2 = n - 2

    fibr1 = fib(n1)
    fibr2 = fib(n2)

    res = fibr1 + fibr2

    return res
