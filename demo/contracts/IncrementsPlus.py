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
    testinvoke fe4a4572c3906dadc3c2ba424d8b972f8f0b99ec show

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
    if operation == 'reset':
        return do_reset()
    elif operation == 'show':
        return do_show()
    elif operation == 'context':
        return do_context()
    elif operation == 'welcome':
        return do_welcome()
    elif operation == 'increase':
        return do_increase()
    elif operation == 'decrease':
        return do_decrease()

    return 'unknown operation'

def get_counter():
    context = GetContext()
    return Get(context, 'counter')

def set_counter(val):
    context = GetContext()
    Put(context, 'counter', val)

def do_show():
    print("show triggered")
    currentCount = get_counter()
    currentCount += 0 # trick value to always be an integer
    return currentCount

def do_context():
    print("context triggered")
    context = GetContext()
    return context

def do_reset():
    print("reset triggered")
    set_counter(0)
    return 0

def do_welcome():
    print("welcome triggered")
    return 'Welcome to Increment2 contract!'

def do_increase():
    print("increase triggered")
    currentCount = get_counter()
    currentCount += 1
    set_counter(currentCount)
    return currentCount

def do_decrease():
    print("decrease triggered")
    currentCount = get_counter()
    currentCount -= 1
    set_counter(currentCount)
    return currentCount
