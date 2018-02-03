"""
MORE WORK NEEDED

Random Test

Test obtaining random generated values via different methods.

Test Command:
    build [FILE_PATH] test 0710 05 True False version
    build ./demo/contracts/RandomTest.py test 0710 05 True False version
    import contract ./demo/contracts/RandomTest.avm 0710 05 True False
Example Executions:
    testinvoke [CONTRACT_HASH] version
False Positive Examples:
Invalid Examples:
"""
from boa.blockchain.vm.Neo.Storage import Get, Put, Delete, GetContext
from boa.blockchain.vm.Neo.Blockchain import GetHeight, GetHeader
from boa.blockchain.vm.Neo.Runtime import Log, Notify, GetTrigger, CheckWitness
from boa.blockchain.vm.Neo.Transaction import GetHash
from boa.blockchain.vm.System.ExecutionEngine import GetScriptContainer

# Global
VERSION = 2

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


def get_block():
    current_height = GetHeight()
    current_block = GetHeader(current_height)
    return current_height
