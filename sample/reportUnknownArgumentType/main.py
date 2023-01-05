"""
- Diagnostics for call arguments for functions or methods that have an unknown type.
- 引数の型が不明です
"""


def _hoge(x: int) -> None:
    del x


x = any()  # type: ignore

_hoge(x)
