"""
Test Command:
    build ./demo/contracts/FourtyFour.py test ff 02 True True

Test Response:
    Calling ./demo/contracts/FourtyFour.py with arguments []
    Test deploy invoke successful
    Used total of 11 operations
    Result 44
    Invoke TX gas cost: 0.001

Import Command:
    import contract ./demo/contracts/FourtyFour.avm ff 02 True True

Import Response:
    Test deploy invoke successful
    Total operations executed: 11
    Results ['IOp Interface: <neo.Core.State.ContractState.ContractState object at 0x106e6a780> ']
    Deploy Invoke TX gas cost: 990.0
    Deploy Invoke TX Fee: 0.0

Expected Opcode:
              3   243                 b'\x03\x00'                                       [data] 3
              6   LOAD_CONST          44                                                [data] 44
              8   NOP                                                                   [data]
              9   241                                                                   [data]
              10  242                                                                   [data]
              11  RETURN_VALUE                                                          [data]

Example Invocation:

Example Response:

"""
def Main():
    return 44
