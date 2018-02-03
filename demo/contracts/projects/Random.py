"""
Test Command:
    build ./demo/contracts/Random.py test 0710 05 True False version

Import Command:
    import contract ./demo/contracts/Random.avm 07 02 True False

Example Invokes:
    testinvoke f9bc3d85ef1ef08d72927b4bb714a0d9d92fccc3 version
"""
from boa.blockchain.vm.Neo.Storage import Get, Put, Delete, GetContext
from boa.blockchain.vm.Neo.Blockchain import GetHeight, GetHeader
from boa.blockchain.vm.Neo.Runtime import Log, Notify, GetTrigger, CheckWitness
from boa.blockchain.vm.Neo.Transaction import GetHash
from boa.blockchain.vm.System.ExecutionEngine import GetScriptContainer

# Global
VERSION = 1

def Main(operation, args):
    """

    :param operation: str The name of the operation to perform
    :param args: list A list of arguments along with the operation
    :return:
        bytearray: The result of the operation
    """
    if operation == 'version':
        return do_version()
    elif operation == 'height':
        return do_height()
    elif operation == 'timestamp':
        return do_timestamp()
    elif operation == 'consensus':
        return do_consensus()
    elif operation == 'random':
        return do_random()
    return 'unknown operation'

def do_version():
    version = VERSION
    return version

def do_height():
    current_height = GetHeight()
    return current_height

def do_timestamp():
    current_block = get_block()
    current_time = current_block.Timestamp
    return current_time

def do_consensus():
    current_block = get_block()
    current_consensus = current_block.ConsensusData
    return current_consensus

def do_random():
    # current_height = GetHeight()
    # Log('current_height:')
    # Log(current_height)
    # current_block = GetHeader(current_height)
    # Log('current_block:')
    # Log(current_block)
    # current_time = current_block.Timestamp
    # Log('current_time:')
    # Log(current_time)
    return False

def get_block():
    current_height = GetHeight()
    current_block = GetHeader(current_height)
    return current_height
