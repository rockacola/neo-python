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

[0] STOP 
[1] STOP 
[2] SDIV 
[29] PUSH26 0x656e637401310a466f75727479466f7572535201ff0c51c56b62 
[30] SUB 
[31] STOP 
[32] ADD 
[33] '2c'(Unknown Opcode) 
[36] PUSH2 0x6c75 
[44] PUSH7 0x68134e656f2e43 

Expected Bytecode:
    00000579656e637401310a466f75727479466f7572535201ff0c51c56b620300012c616c756668134e656f2e436f6e74726163742e437265617465

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
