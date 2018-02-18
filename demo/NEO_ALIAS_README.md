# NeoAlias README

## Summary

``` sh
Test Command:
    build ./demo/contracts/projects/neo-alias.py test 0710 05 True False version

Import Command:
    import contract ./demo/contracts/projects/neo-alias.avm 0710 05 True False

Example Invocation:
    testinvoke 78d5c1ce1f227b987c6650106e7ceb1626b36879 version

TODO:
    - get_safe_str
    - get_safe_int
    - explore the idea of output status code (eg/ 'BAD_AUTH') to provide better diagnostic hints
Performance TODO:
    - tweak structure in a way, where truthy operations should be the shortest path
NOTES:
    - {target_address}_{alias_index}_{invoker_address} = {point}
    - set_alias is currently costing 8+ GAS
KNOWN LIMITATIONS:
    - No duplicate alias detection
```
