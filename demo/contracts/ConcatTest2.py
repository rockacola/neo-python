"""
Data Concatenation Test

A simple utilise contract that attempts to concatenate 2 values together, disregard of their data types.

Test Command:
    build [FILE_PATH] test 0710 05 True False concat ['hey','ho']
    build ./demo/contracts/ConcatTest2.py test 0710 05 True False concat ['hey','ho']

Example Executions:
    testinvoke [CONTRACT_HASH] concat ['lorem','ipsum']
    testinvoke [CONTRACT_HASH] concat ['cloud',9']
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
    :rtype: Union[bool, str]
    """
    if len(args) > 1:
        a = args[0]
        b = args[1]
        output = concat(a, b)
        return output
    Notify('invalid argument length')
    return False
