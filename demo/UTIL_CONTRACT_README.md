# UtilContract README

## Summary

TBA

---

## Example Usages

### Test builds

``` sh
build ./demo/contracts/util-contract.py test 0710 05 True False version
build ./demo/contracts/util-contract.py test 0710 05 True False my_address --attach-gas=0.001
build ./demo/contracts/util-contract.py test 0710 05 True False is_address ['AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y'] --attach-gas=0.001
build ./demo/contracts/util-contract.py test 0710 05 True False is_witness_address ['AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y']
build ./demo/contracts/util-contract.py test 0710 05 True False char_count ['AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y']
```

### Test invokes

``` sh
testinvoke 8322cac3d30094c947615c944e9d3734b6e467bc version
testinvoke 8322cac3d30094c947615c944e9d3734b6e467bc my_address [] --attach-gas=0.001
testinvoke 8322cac3d30094c947615c944e9d3734b6e467bc is_address ['AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y'] --attach-gas=0.001
```

---

## Development notes

### Todo

#### High priority

* Set key-value into context (test non-ASCII characters, and crazy length)
* Get key-value from context
* get string/int/bytearray from global variable
* get string/int/bytearray from local variable

#### Medium priority

* Get current transaction hash
* Get invoker's address
* Get attached asset details
* Get string name of the type of input argument
* Concate 2 values of any datatype together
* Concate n strings together
* String replace
* String indexOf
* Check if a key exists in context
* Array storage example (pop, push, fetch, count)
* Get block timestamp

#### Low priority

TBA
