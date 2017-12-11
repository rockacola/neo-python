import os
import binascii

_file = '/Users/travis/ProjectGit/rockacola/neo-python/demo/contracts/FourtyThree.avm'
with open(_file, "rb") as f:
    stream = f.read()
    f.close
    print("print the bytecode stream:")
    print(binascii.hexlify(stream).decode('ascii'))

"""
Example output for 'FourtyThree.avm':
    51c56b620300012b616c7566
"""
