"""
- Diagnostics for input or return parameters for functions or methods that have an unknown type.
- 引数の型情報が不明です
"""

t1 = hoge_int  # type: ignore


def hoge(x: t1) -> None:
    del x
