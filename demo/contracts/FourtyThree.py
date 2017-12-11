"""
Test Command:
    build ./demo/contracts/FourtyThree.py test ff 02 True

Import Command:
    import contract ./demo/contracts/FourtyThree.avm ff 02 True

Expected Opcode:
              3   243                 b'\x03\x00'                                       [data] 3
              6   LOAD_CONST          43                                                [data] 43
              8   NOP                                                                   [data]
              9   241                                                                   [data]
              10  242                                                                   [data]
              11  RETURN_VALUE                                                          [data]

Example Invocation:
    testinvoke f3aa64eda36f524893c8f941fcf0a132031cf336

Example Response:
    Test invoke successful
    Total operations: 11
    Results ["ByteArray: b'+'"]
    Invoke TX gas cost: 0.0
    Invoke TX Fee: 0.001
"""
def Main():
    """
    :return: 43
    :rtype: int
    """

    return 43
