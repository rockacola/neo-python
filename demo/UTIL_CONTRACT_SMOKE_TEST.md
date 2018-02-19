# Smock Test for UtilContract

## Summary

* Ensure smart contract event is enabled: `config sc-events on`
* Open `neo-privnet` wallet

## Against PrivNet

### General

``` sh
build ./demo/contracts/util-contract.py test 0710 05 True False version
build ./demo/contracts/util-contract.py test 0710 05 True False is_owner
```

### Constant

``` sh
build ./demo/contracts/util-contract.py test 0710 05 True False magic_number
build ./demo/contracts/util-contract.py test 0710 05 True False magic_string
build ./demo/contracts/util-contract.py test 0710 05 True False neo_id
```

### Number


``` sh
build ./demo/contracts/util-contract.py test 0710 05 True False char_count ['AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y']
```

### String

TBA


### Array

TBA


### Storage

``` sh
build ./demo/contracts/util-contract.py test 0710 05 True False set_storage ['lorem','lorem_value']
build ./demo/contracts/util-contract.py test 0710 05 True False get_storage ['lorem']
build ./demo/contracts/util-contract.py test 0710 05 True False set_storage ['current_rate',14.5]
build ./demo/contracts/util-contract.py test 0710 05 True False get_storage ['current_rate']
```

### Block

TBA


### Account

``` sh
build ./demo/contracts/util-contract.py test 0710 05 True False my_address --attach-gas=0.001
build ./demo/contracts/util-contract.py test 0710 05 True False target_address --attach-gas=0.001
build ./demo/contracts/util-contract.py test 0710 05 True False is_address ['AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y'] --attach-gas=0.001
build ./demo/contracts/util-contract.py test 0710 05 True False is_witness_address ['AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y']
```

---

## Against TestNet

``` sh
testinvoke 8322cac3d30094c947615c944e9d3734b6e467bc version
testinvoke 8322cac3d30094c947615c944e9d3734b6e467bc my_address [] --attach-gas=0.001
testinvoke 8322cac3d30094c947615c944e9d3734b6e467bc is_address ['AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y'] --attach-gas=0.001
```
