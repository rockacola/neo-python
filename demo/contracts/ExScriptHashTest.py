"""
Test Command:
    build ./demo/contracts/ExScriptHashTest.py test 07 07 True False lorem

Import Command:
    import contract ./demo/contracts/ExScriptHashTest.avm 07 07 True False

Example Invocation:
    testinvoke 872534652d44eb14d0a0ded3f3e30e0fbea49ebb lorem

"""
from boa.blockchain.vm.Neo.Blockchain import GetAccount, GetAsset
from boa.blockchain.vm.System.ExecutionEngine import GetExecutingScriptHash
from boa.blockchain.vm.Neo.Account import GetBalance
from boa.blockchain.vm.Neo.Runtime import Notify

GAS = b'\xe7-(iy\xeel\xb1\xb7\xe6]\xfd\xdf\xb2\xe3\x84\x10\x0b\x8d\x14\x8ewX\xdeB\xe4\x16\x8bqy,`'


def Main(operation):
    """

    :param operation:
    :return:
    """
    hash = GetExecutingScriptHash()

    Notify(hash)

    account = GetAccount(hash)

    print("account!")

    Notify(account)

    print("will get asset")
    asset = GetAsset(GAS)

    Notify(asset)

    print("will get balance")
    balance = GetBalance(account, GAS)

    Notify(balance)

    return operation
