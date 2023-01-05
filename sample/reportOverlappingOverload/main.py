"""
- Diagnostics for function overloads that overlap in signature and obscure each other or have incompatible return types.
- 不適切な overload の記述があります
"""
from typing import overload, Union


@overload
def hoge(x: int) -> str:
    ...


@overload
def hoge(x: int) -> str:
    ...


def hoge(x: Union[int, str]) -> Union[str, None]:
    if isinstance(x, int):
        return None
    return x
