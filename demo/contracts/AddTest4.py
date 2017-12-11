"""
Test Command:
    build ./demo/contracts/AddTest4.py test 05050505 02 True False 1 2 3 4

Import Command:
    import contract ./demo/contracts/AddTest4.avm 05050505 05 True False

Expected Opcode:
    55c56b6c766b00527ac46c766b51527ac46c766b52527ac46c766b53527ac46203006c766b00c36c766b51c3936c766b52c36c766b53c39594616c7566

Example Invocation:
    testinvoke fcdd63ff10f1f36f86b5a840205fe273664d04f9 1 2 3 4

Example Response:
    Test invoke successful
    Total operations: 65
    Results ['Integer: -9 ']
    Invoke TX gas cost: 0.0
    Invoke TX Fee: 0.001
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
