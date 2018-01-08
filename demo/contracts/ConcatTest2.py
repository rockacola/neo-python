"""
Data Concatenation Test

A simple utilise contract that attempts to concatenate 2 values together, disregard of their data types.

Test Command:
    build [FILE_PATH] test 0710 05 False False concat ['hey','ho']
    build ./demo/contracts/ConcatTest2.py test 0710 05 False False concat ['hey','ho']
    import contract ./demo/contracts/ConcatTest2.avm 0710 05 False False
Example Executions:
    testinvoke [CONTRACT_HASH] concat ['lorem','ipsum']
    testinvoke [CONTRACT_HASH] concat ['cloud',9']
    testinvoke 1c3e9ef16ca1e3927bc663231243a7e0ddd5c818 concat ['lorem','ipsum']
    testinvoke 1c3e9ef16ca1e3927bc663231243a7e0ddd5c818 concat ['cloud',9]
    testinvoke 1c3e9ef16ca1e3927bc663231243a7e0ddd5c818 concat ['text',b'1010']
Invalid Examples:
    testinvoke [CONTRACT_HASH] concat [true,false]
    testinvoke [CONTRACT_HASH] concat ['null',null]
False Positive Examples:
    testinvoke [CONTRACT_HASH] concat [0.9,1.23]
"""
from boa.blockchain.vm.Neo.Storage import Get, Put, Delete, GetContext
from boa.blockchain.vm.Neo.Runtime import Log, Notify
from boa.code.builtins import concat


def Main(operation, args):
    """

    :param operation: The name of the operation to perform
    :param args: A list of arguments along with the operation
    :type operation: str
    :type args: list
    :return: The result of the operation
    :rtype: bytearray
    """
    if operation == 'concat':
        return do_concat(args)
    else:
        Notify('unknown operation')
        return False


def do_concat(args):
    """

    :param args: A list of arguments along with the operation
    :type args: list
    :return: result of combined values
    :rtype: Union[bool, bytearray]
    """
    if len(args) > 1:
        a = args[0]
        b = args[1]
        output = concat(a, b)
        return output
    Notify('invalid argument length')
    return False
