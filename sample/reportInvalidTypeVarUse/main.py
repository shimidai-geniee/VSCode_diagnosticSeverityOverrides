"""
- Diagnostics for improper use of type variables in a function signature.
- TypeVar 変数の使用が不適切です
"""
from typing import TypeVar

T1 = TypeVar("T1")


def hoge(x: T1) -> str:
    return str(x)
