"""
This is to follow NEP5-like contract structure.
REF: https://medium.com/proof-of-working/how-to-build-an-ico-on-neo-with-the-nex-ico-smart-contract-template-1beac1ff0afd
"""
"""
Test Command:
    build ./demo/contracts/IncrementsPlus.py test 0710 05 True False version

Test Response:
    Calling ./demo/contracts/IncrementsPlus.py with arguments ['show']
    Test deploy invoke successful
    Used total of 111 operations
    Result b'\x05'
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
    testinvoke b19ec14fed8dd6f42ab97b3d4de9b98ef9ee5193 show
    testinvoke b19ec14fed8dd6f42ab97b3d4de9b98ef9ee5193 increase [1]

Example Response:
    Test invoke successful
    Total operations: 219
    Results ["ByteArray: bytearray(b'\\x00')", 'Integer: 1 ']
    Invoke TX gas cost: 0.0
    Invoke TX Fee: 0.001
"""
from boa.blockchain.vm.Neo.Storage import Get, Put, Delete, GetContext
from boa.blockchain.vm.Neo.Runtime import Notify

# Global
VERSION = 2

def Main(operation, args):
    """

    :param operation: str The name of the operation to perform
    :param args: list A list of arguments along with the operation
    :return:
        bytearray: The result of the operation
    """
    if operation == 'version':
        return do_version()
    elif operation == 'reset':
        return do_reset()
    elif operation == 'show':
        return do_show()
    elif operation == 'welcome':
        return do_welcome()
    elif operation == 'increase':
        return do_increase(args)
    elif operation == 'decrease':
        return do_decrease(args)

    return 'unknown operation'

def do_version():
    version = VERSION
    Notify(version)
    return version

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

def do_reset():
    print("reset triggered")
    set_counter(0)
    return 0

def do_welcome():
    print("welcome triggered")
    return 'Welcome to Increment2 contract!'

def do_increase(args):
    print("increase triggered")
    if (len(args) > 0):
        val = args[0]
        currentCount = get_counter()
        currentCount += val
        set_counter(currentCount)
        return currentCount
    else:
        print("invalid input args")
        return False

def do_decrease(args):
    print("decrease triggered")
    if (len(args) > 0):
        val = args[0]
        currentCount = get_counter()
        currentCount -= val
        set_counter(currentCount)
        return currentCount
    else:
        print("invalid input args")
        return False
