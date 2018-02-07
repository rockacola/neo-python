"""
Test Command:
    build ./demo/contracts/get-version.py test 0710 05 True False version

Import Command:
    import contract ./demo/contracts/get-version.avm 0710 05 True False

Example Invocation:
    testinvoke a48bc0f99caed8b0f76cee42ab9d91f235825f85 version
"""
from boa.blockchain.vm.System.ExecutionEngine import GetScriptContainer, GetExecutingScriptHash
from boa.blockchain.vm.Neo.Transaction import *
from boa.blockchain.vm.Neo.Runtime import Log, Notify, GetTrigger, CheckWitness
from boa.blockchain.vm.Neo.Blockchain import GetHeight, GetHeader
from boa.blockchain.vm.Neo.Action import RegisterAction
from boa.blockchain.vm.Neo.TriggerType import Application, Verification
from boa.blockchain.vm.Neo.Storage import GetContext, Get, Put, Delete
from boa.blockchain.vm.Neo.Output import GetScriptHash, GetValue, GetAssetId
from boa.code.builtins import concat, list, range, take, substr


# Global
VERSION = 7
OWNER = b'#\xba\'\x03\xc52c\xe8\xd6\xe5"\xdc2 39\xdc\xd8\xee\xe9' # script hash for address: AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y


def Main(operation: str, args: list) -> bytearray:
    trigger = GetTrigger()

    if trigger == Verification():
        is_owner = CheckWitness(OWNER)
        if is_owner:
            return True
        return False

    elif trigger == Application():
        if operation == 'version':
            result = get_version()
            return result
        elif operation == 'version2':
            result = get_version2()
            return result
        elif operation == 'version3':
            result = get_version2()
            return result

        Log('unknown operation')
        return False

    Log('invalid request')
    return False

def get_version() -> int:
    version = VERSION
    Notify(version)
    return version

def get_version2() -> int:
    version = 0 + VERSION
    Notify(version)
    return version

def get_version3() -> int:
    version = 7
    Notify(version)
    return version
