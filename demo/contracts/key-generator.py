"""
Test Command:
    build ./demo/contracts/key-generator.py test 0710 05 True False version

Import Command:
    import contract ./demo/contracts/key-generator.avm 0710 05 True False

Example Invocation:
    testinvoke 160c4f042e442266df8376082ab40b7c71c5e186 version
    testinvoke 160c4f042e442266df8376082ab40b7c71c5e186 keygen ['prefix_',2]

URL: https://pastebin.com/vfWFcBBT
"""
from boa.blockchain.vm.Neo.Runtime import Log, Notify, GetTrigger, CheckWitness
from boa.blockchain.vm.Neo.TriggerType import Application, Verification
from boa.code.builtins import concat


# Global
VERSION = 8
OWNER = b'#\xba\'\x03\xc52c\xe8\xd6\xe5"\xdc2 39\xdc\xd8\xee\xe9'  # script hash for address: AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y
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
        elif operation == 'is_owner':       # Checking if invoker is the owner of the smart contract
            result = do_is_owner()
            return result
        elif operation =='keygen':
            result = do_keygen(args)
            return result
        
        Log('unknown operation')
        return False

    Log('invalid request')
    return False


def do_version() -> int:
    version = VERSION
    Notify(version)
    return version


def do_is_owner() -> bool:
    return CheckWitness(OWNER)


def do_keygen(args: list) -> str:
    if len(args) > 1:
        prefix = args[0]
        index = args[1]
        Log('prefix:')
        Log(prefix)
        Log('index:')
        Log(index)
        key = concat(prefix, index)
        Log('key:')
        Log(key)
        return key
    Notify('invalid argument length')
    return False
