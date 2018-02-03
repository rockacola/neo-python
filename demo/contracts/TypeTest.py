"""
NOT WORKING

Type Test

Test data type of the input argument.

Test Command:
    build [FILE_PATH] test 10 07 False False lorem
    build ./demo/contracts/TypeTest.py test 10 07 False False lorem
    import contract ./demo/contracts/TypeTest.avm 10 07 False False
Example Executions:
    testinvoke [CONTRACT_HASH] lorem
    testinvoke ba9f94243b0aa41bae1d8203c432717dfae8db26 lorem
False Positive Examples:
Invalid Examples:
"""
from boa.blockchain.vm.Neo.Transaction import *

def Main(input):
    """

    :param input: The string to count characters
    :type operation: str
    :return: The length of the input string
    :rtype: number
    """
    inputType = GetType(input)
    return inputType
