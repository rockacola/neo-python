"""
NeoAlias Smart Contract

Give alias to wallet addresses

"""
"""
Test Command:
    build ./demo/contracts/NeoAlias.py test 0710 05 True False version

Import Command:
    import contract ./demo/contracts/NeoAlias.avm 0710 05 True False

Example Invocation:
    testinvoke 4b96787b1a2f7f11cebdf2f3c5cf2899e1a1886a version

More Example Invokes:
    testinvoke 4b96787b1a2f7f11cebdf2f3c5cf2899e1a1886a is_owner
    testinvoke 4b96787b1a2f7f11cebdf2f3c5cf2899e1a1886a get_trigger
    testinvoke 4b96787b1a2f7f11cebdf2f3c5cf2899e1a1886a get_tx
"""
from boa.blockchain.vm.Neo.Storage import Get, Put, Delete, GetContext
from boa.blockchain.vm.Neo.Runtime import Log, Notify, CheckWitness

# Global
VERSION = 1
OWNER = b'#\xba\'\x03\xc52c\xe8\xd6\xe5"\xdc2 39\xdc\xd8\xee\xe9' # script hash for address: AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y

def Main(operation, args):
    """

    :param operation: str The name of the operation to perform
    :param args: list A list of arguments along with the operation
    :return:
        bytearray: The result of the operation
    """
    if operation == 'version':
        return do_version()
    elif operation == 'is_owner':
        return do_is_owner()
    return 'unknown operation'

def do_version():
    version = VERSION
    Notify(version)
    return version

def do_is_owner():
    return CheckWitness(OWNER)
