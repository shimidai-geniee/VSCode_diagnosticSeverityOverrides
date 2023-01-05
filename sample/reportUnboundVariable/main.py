"""
- Diagnostics for unbound and possibly unbound variables.
- 参照できない変数が生じ得ます
"""


def hoge(flag: bool) -> int:
    if flag:
        x = 1
    return x
