# neo-python demo

## Get Started

* Start prompt: `python3 prompt.py -p`
* To open demo wallet: `open wallet ./demo/wallets/neo-privnet.wallet`
* To force sync of the wallet: `wallet rebuild`
* To lint: `pycodestyle [FILE_PATH]`

### Wallets

#### neo-privnet

* Address: `AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y`
* WIF: `KxDgvEKzgSBPPfuVfw67oPQBSjidEiqTHURKSDL1R7yGaGYAeYnr`
* Password: `coz`
* Script hash: `b'#\xba\'\x03\xc52c\xe8\xd6\xe5"\xdc2 39\xdc\xd8\xee\xe9'`

#### alfa

* Address: `AbXMJ6JK494Q7QXuoM6H7s2LgotNWZe9XX`
* WIF: `...`
* Password: `1234567890`
* Script hash: `b'\xd8\xa3[\x14L\xa8\xd3\xfa\x00\xad\x83T\xed\xd2\x87G\xfb_\xffJ'`

## Developer References

To see list of opcodes:

* `/neo-python/neo/VM/OpCode.py`, or
* `/neo-boa/boa/blockchain/vm/VMOp.py`

To see list of type values:

* `/neo-python/neo/SmartContract/ContractParameterType.py`

``` py
Signature = 0x00        # 签名
Boolean = 0x01
Integer = 0x02          # 整数
Hash160 = 0x03          # 160位散列值
Hash256 = 0x04          # 256位散列值
ByteArray = 0x05        # 字节数组
PublicKey = 0x06
String = 0x07
Array = 0x10
Void = 0xff
```
