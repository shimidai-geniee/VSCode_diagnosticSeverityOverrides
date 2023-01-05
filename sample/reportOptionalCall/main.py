"""
- Diagnostics for an attempt to call a variable with an Optional type.
- None に対して呼び出ししないで
"""
import random


class _Hoge:
    pass


ins = None if random.random() > 0.5 else _Hoge
_ = ins()
