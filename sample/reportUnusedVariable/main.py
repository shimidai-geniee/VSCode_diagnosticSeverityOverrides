"""
- Diagnostics for a variable that is not accessed.
- 使われない変数があります
"""


def _hoge() -> None:
    x = 1


del _hoge
