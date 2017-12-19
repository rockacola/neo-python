# neo-python demo

## Get Started

* To open demo wallet: `open wallet ./demo/wallets/neo-privnet.wallet`
* To force sync of the wallet: `wallet rebuild`

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
