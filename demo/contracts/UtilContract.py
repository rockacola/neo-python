"""
Test Command:
    build ./demo/contracts/UtilContract.py test 0710 05 True False version

Import Command:
    import contract ./demo/contracts/UtilContract.avm 0710 05 True False

Example Invocation:
    testinvoke 4f74c41ce60dcc8abb6f5b396935430f9d3b1db1 version

More Example Invokes:
    testinvoke 4f74c41ce60dcc8abb6f5b396935430f9d3b1db1 is_owner
    testinvoke 4f74c41ce60dcc8abb6f5b396935430f9d3b1db1 my_address
"""
from boa.blockchain.vm.System.ExecutionEngine import GetScriptContainer,GetExecutingScriptHash
from boa.blockchain.vm.Neo.Transaction import *
from boa.blockchain.vm.Neo.Runtime import Log, Notify, GetTrigger, CheckWitness
from boa.blockchain.vm.Neo.Blockchain import GetHeight, GetHeader
from boa.blockchain.vm.Neo.Action import RegisterAction
from boa.blockchain.vm.Neo.TriggerType import Application, Verification
from boa.blockchain.vm.Neo.Storage import GetContext, Get, Put, Delete
from boa.blockchain.vm.Neo.Output import GetScriptHash,GetValue,GetAssetId
from boa.code.builtins import concat, list, range, take, substr


# Global
VERSION = 1
OWNER = b'#\xba\'\x03\xc52c\xe8\xd6\xe5"\xdc2 39\xdc\xd8\xee\xe9' # script hash for address: AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y
# NEO_ASSET_ID = b'\x9b|\xff\xda\xa6t\xbe\xae\x0f\x93\x0e\xbe`\x85\xaf\x90\x93\xe5\xfeV\xb3J\\"\x0c\xcd\xcfn\xfc3o\xc5'
# GAS_ASSET_ID = b'\xe7-(iy\xeel\xb1\xb7\xe6]\xfd\xdf\xb2\xe3\x84\x10\x0b\x8d\x14\x8ewX\xdeB\xe4\x16\x8bqy,`'


def Main(operation: str, args: list) -> bytearray:
    trigger = GetTrigger()

    if trigger == Verification():
        is_owner = CheckWitness(OWNER)
        Log('Check is_owner:')
        Log(is_owner)
        if is_owner:
            return True
        return False

    elif trigger == Application():
        if operation == 'version':
            result = do_version()
            return result
        elif operation == 'is_owner':
            result = do_is_owner()
            return result
        elif operation == 'my_address':
            result = do_my_address()
            return result
        Log('unknown operation')
        return False

    Log('invalid request')
    return False


def do_version() -> bytearray:
    version = VERSION
    Notify(version)
    return version


def do_is_owner() -> bytearray:
    return CheckWitness(OWNER)


def do_my_address() -> bytearray:
    # This is not working
    tx = GetScriptContainer()
    refs = tx.References
    ref = refs[0]
    Log('ref:')
    Log(ref)
    sentAsset = GetAssetId(ref)
    Log('sentAsset:')
    Log(sentAsset)
    sender = GetScriptHash(ref)
    Log('sender:')
    Log(sender)
    Notify('Not implemented.')
    return False
