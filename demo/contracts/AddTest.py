"""
Since: 2017-12-11

Test Command:
    build ./demo/contracts/AddTest.py test 0505 02 True True 1 2

Import Command:
    import contract ./demo/contracts/AddTest.avm 0505 05 True True

Expected Opcode:
              17  LOAD_FAST           a                                                 [data]
              22  LOAD_FAST           b                                                 [data]
              27  BINARY_ADD                                                            [data]
              28  STORE_FAST          c                                                 [data]


19            35  243                 b'\x03\x00'                                       [data] 3
              38  LOAD_FAST           c                                                 [data]
              43  NOP                                                                   [data]
              44  241                                                                   [data]
              45  242                                                                   [data]
              46  RETURN_VALUE                                                          [data]

Example Invocation:
    testinvoke 28dfdb9d1d0fa0b86804e4a4e0f0c42484f32792 7 9

Example Response:
    Test invoke successful
    Total operations: 49
    Results ['Integer: 16 ']
    Invoke TX gas cost: 0.0
    Invoke TX Fee: 0.001
"""
def Main(a, b):
    """
    :param a: an integer
    :param b: an integer
    :return: a + b
    :rtype: int
    """

    c = a + b

    return c
