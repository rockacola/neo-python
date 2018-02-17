# Smock Test for NeoAlias

## Summary

TBA

## Against PrivNet

TBA

## Aginst TestNet

TBA


----------------------------------------

## Legacy

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
build ./demo/contracts/projects/neo-alias.py test 0710 05 True False count_alias ['addr1']
build ./demo/contracts/projects/neo-alias.py test 0710 05 True False get_alias ['addr1',1]
```

* Realistic alias assignment

```
build ./demo/contracts/projects/neo-alias.py test 0710 05 True False set_alias ['AYUhHYViEoXEWeLQsXU9y1taps4nvjAHiy','yuri']
build ./demo/contracts/projects/neo-alias.py test 0710 05 True False set_alias ['AYUhHYViEoXEWeLQsXU9y1taps4nvjAHiy','yuri2']
build ./demo/contracts/projects/neo-alias.py test 0710 05 True False set_alias ['AZLvNpvTmDvEL4Qc5AH64vniSJe11LHzWU','zera']
build ./demo/contracts/projects/neo-alias.py test 0710 05 True False count_alias ['AYUhHYViEoXEWeLQsXU9y1taps4nvjAHiy']
build ./demo/contracts/projects/neo-alias.py test 0710 05 True False get_alias ['AYUhHYViEoXEWeLQsXU9y1taps4nvjAHiy',1]
```

* Stress test on various of alias format

** Can't have space character

```
build ./demo/contracts/projects/neo-alias.py test 0710 05 True False set_alias ['AVmVCX76hYzpZnx5mZV7JcxKpPBHVnyzjd','vicky-vim']
build ./demo/contracts/projects/neo-alias.py test 0710 05 True False set_alias ['AVmVCX76hYzpZnx5mZV7JcxKpPBHVnyzjd','Victa m. Veon']  # Fails
build ./demo/contracts/projects/neo-alias.py test 0710 05 True False set_alias ['AVmVCX76hYzpZnx5mZV7JcxKpPBHVnyzjd','Vic Veon']  # Fails
build ./demo/contracts/projects/neo-alias.py test 0710 05 True False set_alias ['AVmVCX76hYzpZnx5mZV7JcxKpPBHVnyzjd','Van.Von']
build ./demo/contracts/projects/neo-alias.py test 0710 05 True False set_alias ['AVmVCX76hYzpZnx5mZV7JcxKpPBHVnyzjd','Ven签名']
build ./demo/contracts/projects/neo-alias.py test 0710 05 True False count_alias ['AVmVCX76hYzpZnx5mZV7JcxKpPBHVnyzjd']
build ./demo/contracts/projects/neo-alias.py test 0710 05 True False get_alias ['AVmVCX76hYzpZnx5mZV7JcxKpPBHVnyzjd',0]
```

* Vote

```
build ./demo/contracts/projects/neo-alias.py test 0710 05 True False vote_alias ['AYUhHYViEoXEWeLQsXU9y1taps4nvjAHiy',0,1] --attach-gas=0.001
build ./demo/contracts/projects/neo-alias.py test 0710 05 True False get_alias_score ['AYUhHYViEoXEWeLQsXU9y1taps4nvjAHiy',0]
```

### Smoke tests on Testnet

* Start by checking the alias counts

```
testinvoke 8da85fb01a367bc214482d11c929d8ee5f090bcf count_all
testinvoke 8da85fb01a367bc214482d11c929d8ee5f090bcf count_alias ['AYUhHYViEoXEWeLQsXU9y1taps4nvjAHiy']
```

* Assign some aliases to few addresses

```
testinvoke 8da85fb01a367bc214482d11c929d8ee5f090bcf set_alias ['AYUhHYViEoXEWeLQsXU9y1taps4nvjAHiy','yuri']
testinvoke 8da85fb01a367bc214482d11c929d8ee5f090bcf set_alias ['AYUhHYViEoXEWeLQsXU9y1taps4nvjAHiy','yuri2']
testinvoke 8da85fb01a367bc214482d11c929d8ee5f090bcf set_alias ['AZLvNpvTmDvEL4Qc5AH64vniSJe11LHzWU','zera']
testinvoke 8da85fb01a367bc214482d11c929d8ee5f090bcf count_alias ['AYUhHYViEoXEWeLQsXU9y1taps4nvjAHiy']
testinvoke 8da85fb01a367bc214482d11c929d8ee5f090bcf get_alias ['AYUhHYViEoXEWeLQsXU9y1taps4nvjAHiy',1]
testinvoke 8da85fb01a367bc214482d11c929d8ee5f090bcf count_alias ['AZLvNpvTmDvEL4Qc5AH64vniSJe11LHzWU']
```

* Vote alias

```
testinvoke 8da85fb01a367bc214482d11c929d8ee5f090bcf vote_alias ['AYUhHYViEoXEWeLQsXU9y1taps4nvjAHiy',0,1]
testinvoke 8da85fb01a367bc214482d11c929d8ee5f090bcf get_alias_score ['AYUhHYViEoXEWeLQsXU9y1taps4nvjAHiy',0]
```
