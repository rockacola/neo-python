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

## Against TestNet

### Global attributes

``` sh
testinvoke ee235dae59a99e80c1b6cfa0f70bb674d2e87cbf version
testinvoke ee235dae59a99e80c1b6cfa0f70bb674d2e87cbf is_owner
testinvoke ee235dae59a99e80c1b6cfa0f70bb674d2e87cbf count_all
testinvoke ee235dae59a99e80c1b6cfa0f70bb674d2e87cbf get_storage ['all_\x00']
```

### Alias assignments

* Cannot have space characters
* UTF-8 characters seems fine

``` sh
testinvoke ee235dae59a99e80c1b6cfa0f70bb674d2e87cbf count_alias ['AYUhHYViEoXEWeLQsXU9y1taps4nvjAHiy']
testinvoke ee235dae59a99e80c1b6cfa0f70bb674d2e87cbf get_alias ['AYUhHYViEoXEWeLQsXU9y1taps4nvjAHiy',0]
testinvoke ee235dae59a99e80c1b6cfa0f70bb674d2e87cbf set_alias ['AVUfegS354LWRoBuCzuKjGCYkT3tnpFFTD','AYUhHYViEoXEWeLQsXU9y1taps4nvjAHiy','ayu']

testinvoke ee235dae59a99e80c1b6cfa0f70bb674d2e87cbf count_alias ['AZLvNpvTmDvEL4Qc5AH64vniSJe11LHzWU']
testinvoke ee235dae59a99e80c1b6cfa0f70bb674d2e87cbf get_alias ['AZLvNpvTmDvEL4Qc5AH64vniSJe11LHzWU',0]
testinvoke ee235dae59a99e80c1b6cfa0f70bb674d2e87cbf set_alias ['AVUfegS354LWRoBuCzuKjGCYkT3tnpFFTD','AZLvNpvTmDvEL4Qc5AH64vniSJe11LHzWU','azrel.adams']
testinvoke ee235dae59a99e80c1b6cfa0f70bb674d2e87cbf set_alias ['AVUfegS354LWRoBuCzuKjGCYkT3tnpFFTD','AZLvNpvTmDvEL4Qc5AH64vniSJe11LHzWU','azrel.adams签名']
```

### Alias score check

``` sh
testinvoke ee235dae59a99e80c1b6cfa0f70bb674d2e87cbf get_alias_score ['AYUhHYViEoXEWeLQsXU9y1taps4nvjAHiy',0]
testinvoke ee235dae59a99e80c1b6cfa0f70bb674d2e87cbf get_alias_score ['AZLvNpvTmDvEL4Qc5AH64vniSJe11LHzWU',0]
```

### Cast votes

```sh
testinvoke ee235dae59a99e80c1b6cfa0f70bb674d2e87cbf vote_alias ['AVUfegS354LWRoBuCzuKjGCYkT3tnpFFTD','AYUhHYViEoXEWeLQsXU9y1taps4nvjAHiy',0,1]
testinvoke ee235dae59a99e80c1b6cfa0f70bb674d2e87cbf get_alias_score ['AYUhHYViEoXEWeLQsXU9y1taps4nvjAHiy',0]
```

Cast vote with a mismatch invoker address

```sh
testinvoke ee235dae59a99e80c1b6cfa0f70bb674d2e87cbf vote_alias ['BAD','AYUhHYViEoXEWeLQsXU9y1taps4nvjAHiy',0,1]
```