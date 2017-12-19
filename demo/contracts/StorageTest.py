"""
Test Command:
    build ./demo/contracts/StorageTest.py test ff 07 True False

Test Response:

Import Command:

Import Response:

Example Invocation:

Example Response:

"""
from boa.blockchain.vm.Neo.Storage import Get, Put, Delete, GetContext
from boa.blockchain.vm.Neo.Runtime import Notify


def Main():
    """

    :return:
    """
    context = GetContext()

    print("hello")
    Notify(context)

    item_key = 'hello'
    item_val = 'hhhhhhh'
    Notify(item_val)
    Put(context, item_key, item_val)
    print("hhhh")
    a = 1

    out = Get(context, item_key)

    return out
