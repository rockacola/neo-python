# Smock Test for NeoAlias

## Summary

* Ensure smart contract event is enabled: `config sc-events on`
* Open piccolo wallet

## Against PrivNet

### Global attributes

``` sh
build ./demo/contracts/projects/neo-alias.py test 0710 05 True False version
build ./demo/contracts/projects/neo-alias.py test 0710 05 True False is_owner
build ./demo/contracts/projects/neo-alias.py test 0710 05 True False count_all
build ./demo/contracts/projects/neo-alias.py test 0710 05 True False get_all_index [0]
build ./demo/contracts/projects/neo-alias.py test 0710 05 True False get_storage ['all_\x00']
```

### Alias assignments

* Cannot have space characters
* UTF-8 characters seems fine

``` sh
build ./demo/contracts/projects/neo-alias.py test 0710 05 True False count_alias ['AYUhHYViEoXEWeLQsXU9y1taps4nvjAHiy']
build ./demo/contracts/projects/neo-alias.py test 0710 05 True False get_alias ['AYUhHYViEoXEWeLQsXU9y1taps4nvjAHiy',0]
build ./demo/contracts/projects/neo-alias.py test 0710 05 True False set_alias ['AVUfegS354LWRoBuCzuKjGCYkT3tnpFFTD','AYUhHYViEoXEWeLQsXU9y1taps4nvjAHiy','ayu']

build ./demo/contracts/projects/neo-alias.py test 0710 05 True False count_alias ['AZLvNpvTmDvEL4Qc5AH64vniSJe11LHzWU']
build ./demo/contracts/projects/neo-alias.py test 0710 05 True False get_alias ['AZLvNpvTmDvEL4Qc5AH64vniSJe11LHzWU',0]
build ./demo/contracts/projects/neo-alias.py test 0710 05 True False set_alias ['AVUfegS354LWRoBuCzuKjGCYkT3tnpFFTD','AZLvNpvTmDvEL4Qc5AH64vniSJe11LHzWU','azrel.adams']
build ./demo/contracts/projects/neo-alias.py test 0710 05 True False set_alias ['AVUfegS354LWRoBuCzuKjGCYkT3tnpFFTD','AZLvNpvTmDvEL4Qc5AH64vniSJe11LHzWU','azrel.adams签名']
```

### Alias score check

``` sh
build ./demo/contracts/projects/neo-alias.py test 0710 05 True False get_alias_score ['AYUhHYViEoXEWeLQsXU9y1taps4nvjAHiy',0]
build ./demo/contracts/projects/neo-alias.py test 0710 05 True False get_alias_score ['AZLvNpvTmDvEL4Qc5AH64vniSJe11LHzWU',0]
```

### Cast votes

```sh
build ./demo/contracts/projects/neo-alias.py test 0710 05 True False vote_alias ['AVUfegS354LWRoBuCzuKjGCYkT3tnpFFTD','AYUhHYViEoXEWeLQsXU9y1taps4nvjAHiy',0,1]
build ./demo/contracts/projects/neo-alias.py test 0710 05 True False get_alias_score ['AYUhHYViEoXEWeLQsXU9y1taps4nvjAHiy',0]
```

Cast vote with a mismatch invoker address

```sh
build ./demo/contracts/projects/neo-alias.py test 0710 05 True False vote_alias ['BAD','AYUhHYViEoXEWeLQsXU9y1taps4nvjAHiy',0,1]
```

Switch to `neo-privnet.wallet` for casting vote

```sh
build ./demo/contracts/projects/neo-alias.py test 0710 05 True False vote_alias ['AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y','AYUhHYViEoXEWeLQsXU9y1taps4nvjAHiy',0,1]
build ./demo/contracts/projects/neo-alias.py test 0710 05 True False get_alias_score ['AYUhHYViEoXEWeLQsXU9y1taps4nvjAHiy',0]
```

---

## Against TestNet

### Global attributes

``` sh
testinvoke 8a092d91a822192b20e91722dc3dea28dfdb5cbd version
testinvoke 8a092d91a822192b20e91722dc3dea28dfdb5cbd is_owner
testinvoke 8a092d91a822192b20e91722dc3dea28dfdb5cbd count_all
testinvoke 8a092d91a822192b20e91722dc3dea28dfdb5cbd get_storage ['all_\x00']
```

### Alias assignments

* Cannot have space characters
* UTF-8 characters seems fine

``` sh
testinvoke 8a092d91a822192b20e91722dc3dea28dfdb5cbd count_alias ['AYUhHYViEoXEWeLQsXU9y1taps4nvjAHiy']
testinvoke 8a092d91a822192b20e91722dc3dea28dfdb5cbd get_alias ['AYUhHYViEoXEWeLQsXU9y1taps4nvjAHiy',0]
testinvoke 8a092d91a822192b20e91722dc3dea28dfdb5cbd set_alias ['AVUfegS354LWRoBuCzuKjGCYkT3tnpFFTD','AYUhHYViEoXEWeLQsXU9y1taps4nvjAHiy','ayu']

testinvoke 8a092d91a822192b20e91722dc3dea28dfdb5cbd count_alias ['AZLvNpvTmDvEL4Qc5AH64vniSJe11LHzWU']
testinvoke 8a092d91a822192b20e91722dc3dea28dfdb5cbd get_alias ['AZLvNpvTmDvEL4Qc5AH64vniSJe11LHzWU',0]
testinvoke 8a092d91a822192b20e91722dc3dea28dfdb5cbd set_alias ['AVUfegS354LWRoBuCzuKjGCYkT3tnpFFTD','AZLvNpvTmDvEL4Qc5AH64vniSJe11LHzWU','azrel.adams']
testinvoke 8a092d91a822192b20e91722dc3dea28dfdb5cbd set_alias ['AVUfegS354LWRoBuCzuKjGCYkT3tnpFFTD','AZLvNpvTmDvEL4Qc5AH64vniSJe11LHzWU','azrel.adams签名']
```

### Alias score check

``` sh
testinvoke 8a092d91a822192b20e91722dc3dea28dfdb5cbd get_alias_score ['AYUhHYViEoXEWeLQsXU9y1taps4nvjAHiy',0]
testinvoke 8a092d91a822192b20e91722dc3dea28dfdb5cbd get_alias_score ['AZLvNpvTmDvEL4Qc5AH64vniSJe11LHzWU',0]
```

### Cast votes

```sh
testinvoke 8a092d91a822192b20e91722dc3dea28dfdb5cbd vote_alias ['AVUfegS354LWRoBuCzuKjGCYkT3tnpFFTD','AYUhHYViEoXEWeLQsXU9y1taps4nvjAHiy',0,1]
testinvoke 8a092d91a822192b20e91722dc3dea28dfdb5cbd get_alias_score ['AYUhHYViEoXEWeLQsXU9y1taps4nvjAHiy',0]
```

Cast vote with a mismatch invoker address

```sh
testinvoke 8a092d91a822192b20e91722dc3dea28dfdb5cbd vote_alias ['BAD','AYUhHYViEoXEWeLQsXU9y1taps4nvjAHiy',0,1]
```

Switch to `neo-privnet.wallet` for casting vote

```sh
testinvoke 8a092d91a822192b20e91722dc3dea28dfdb5cbd vote_alias ['AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y','AYUhHYViEoXEWeLQsXU9y1taps4nvjAHiy',0,1]
testinvoke 8a092d91a822192b20e91722dc3dea28dfdb5cbd get_alias_score ['AYUhHYViEoXEWeLQsXU9y1taps4nvjAHiy',0]
```
