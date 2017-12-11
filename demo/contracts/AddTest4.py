"""
Test Command:
    build ./demo/contracts/AddTest4.py test 05050505 02 True 1 2 3 4

Import Command:
    import contract ./demo/contracts/AddTest4.avm 05050505 05 True

Expected Opcode:

Example Invocation:

Example Response:

"""

def Main(a, b, c, d):
    """

    :param a:
    :param b:
    :param c:
    :param d:
    :return:
    """
    return a + b - c * d
