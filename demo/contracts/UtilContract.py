"""
TODO:
- Add n numbers together
- Get 2^n
- Get Fibonacci
- Get current block height
- Get current transaction hash
- Get invoker's address
- Get attached asset details
- Get string name of the type of input argument

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
        elif operation == 'is_owner':   # Checking if invoker is the owner of the smart contract
            result = do_is_owner()
            return result
        elif operation == 'length':     # Get length of input arguments array
            result = do_length(args)
            return result
        elif operation == 'add':        # Adding 2 numbers together
            result = do_add(args)
            return result
        elif operation == 'square':     # Returns square of a given value
            result = do_square(args)
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


def do_length(args: list) -> int:
    result = len(args)
    return result


def do_add(args: list) -> int:
    if len(args) > 1:
        n1 = args[0]
        n2 = args[1]
        result = n1 + n2
        return result
    Notify('invalid argument length')
    return False


def do_square(args: list) -> int:
    if len(args) > 0:
        val = args[0]
        result = val * val
        return result
    Notify('invalid argument length')
    return False
