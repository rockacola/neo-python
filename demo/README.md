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

#### piccolo

* Address: `AVUfegS354LWRoBuCzuKjGCYkT3tnpFFTD`
* WIF: `L3QKsExhzK7VXVeEKidZuJgsXLHVoTTNRRU9mQVdnwRkpRhbXG38`
* Password: `1234567890`
* Script hash: `b'\\x96P\\xac\\xd6\\xb7S,\\xb4\\xeaiU\\xedK\\x0f\\xd3\\xaa\\xa9\\xc9Q\\x87'`
* Should have ~2000 GAS in testnet

---

## Development Notes

## Start a fresh docker container

### Re-download/update container

* `docker stop neo-privnet-with-gas`
* `docker rm neo-privnet-with-gas`
* `docker pull metachris/neo-privnet-with-gas`
* `docker run -d --name neo-privnet-with-gas -p 20333-20336:20333-20336/tcp -p 30333-30336:30333-30336/tcp metachris/neo-privnet-with-gas`

### Remove existing chain

* `cd /Users/travis/ProjectGit/rockacola/neo-python`
* `rm -rf Chains/privnet`

You should now have a fresh blockchain ready to go.


## Import wallet using WIF

* `import wif [WIF]`

## In order to claim GAS

* Make a transaction to yourself. That can be achieved by sending NEO to yourself:
  * `send NEO AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y 1`
* Execute `wallet`, notice the `claim.unavailable` value changed over to `claim.available`.
* Claim GAS by: `wallet claim`

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
