# neo-python demo

## Get Started

* Install dependencies: `pip3 install -r requirements.txt`
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

---

## Development Notes

### To know

* How can I obtain invoker's wallet address, in byte array and string
* Learn how to convert bytecode script hash into contract hash
* Learn how to convert private key into wallet public key into wallet hash
* Get random working, via different methods

---

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

### Address looking string

* `AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y`
* `Alice00000000000000000000000000000` (bad)
* `Bob0000000000000000000000000000000` (bad)
* `AYUhHYViEoXEWeLQsXU9y1taps4nvjAHiy`
* `AZLvNpvTmDvEL4Qc5AH64vniSJe11LHzWU`
* `AVmVCX76hYzpZnx5mZV7JcxKpPBHVnyzjd`

### More example executions

```

build ./demo/contracts/projects/neo-alias.py test 0710 05 True False count_alias ['AYUhHYViEoXEWeLQsXU9y1taps4nvjAHiy']
build ./demo/contracts/projects/neo-alias.py test 0710 05 True False set_alias ['AYUhHYViEoXEWeLQsXU9y1taps4nvjAHiy','ayu']
build ./demo/contracts/projects/neo-alias.py test 0710 05 True False set_alias ['AZLvNpvTmDvEL4Qc5AH64vniSJe11LHzWU','azul']

```

### Smoke tests on Privnet

* Start by checking the alias counts

```
build ./demo/contracts/projects/neo-alias.py test 0710 05 True False version
build ./demo/contracts/projects/neo-alias.py test 0710 05 True False count_all
build ./demo/contracts/projects/neo-alias.py test 0710 05 True False count_alias ['AYUhHYViEoXEWeLQsXU9y1taps4nvjAHiy']
```

* Non realistic alias assignment

```
build ./demo/contracts/projects/neo-alias.py test 0710 05 True False set_alias ['addr1','aliasA']
build ./demo/contracts/projects/neo-alias.py test 0710 05 True False set_alias ['addr1','aliasB']
build ./demo/contracts/projects/neo-alias.py test 0710 05 True False set_alias ['addr2','aliasC']
```



### Smoke tests on Testnet

* Start by checking the alias counts

```
testinvoke 6d6491ff4bde82644805c52124798034aa5b2e9f count_all
testinvoke 6d6491ff4bde82644805c52124798034aa5b2e9f count_alias ['AYUhHYViEoXEWeLQsXU9y1taps4nvjAHiy']
```

* Assign some aliases to few addresses

```
testinvoke 6d6491ff4bde82644805c52124798034aa5b2e9f set_alias ['AYUhHYViEoXEWeLQsXU9y1taps4nvjAHiy','yuri']
testinvoke 6d6491ff4bde82644805c52124798034aa5b2e9f set_alias ['AYUhHYViEoXEWeLQsXU9y1taps4nvjAHiy','yuri2']
testinvoke 6d6491ff4bde82644805c52124798034aa5b2e9f set_alias ['AZLvNpvTmDvEL4Qc5AH64vniSJe11LHzWU','zera']
```

