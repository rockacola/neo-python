"""
String Length Test

A simple utilise contract that counts number of characters of provided string

Test Command:
    build [FILE_PATH] test 07 02 False False lorem
    build ./demo/contracts/StringLengthTest.py test 07 02 False False lorem
    import contract ./demo/contracts/StringLengthTest.avm 07 02 False False
Example Executions:
    testinvoke [CONTRACT_HASH] lorem
    testinvoke d757dfd49e86665105cc51d640ec1d11c3c88f9d lorem
    testinvoke d757dfd49e86665105cc51d640ec1d11c3c88f9d a-b
False Positive Examples:
    testinvoke d757dfd49e86665105cc51d640ec1d11c3c88f9d
    testinvoke d757dfd49e86665105cc51d640ec1d11c3c88f9d 3-1
    testinvoke d757dfd49e86665105cc51d640ec1d11c3c88f9d a b
Invalid Examples:
    testinvoke d757dfd49e86665105cc51d640ec1d11c3c88f9d 100-10
"""
def Main(input):
    """

    :param input: The string to count characters
    :type operation: str
    :return: The length of the input string
    :rtype: number
    """
    if not input: # None check
        return 0
    else:
        length = len(input)
        return length
