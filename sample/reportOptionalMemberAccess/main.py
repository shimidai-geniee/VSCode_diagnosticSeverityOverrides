"""
- Diagnostics for an attempt to access a member of a variable with an Optional type.
- None に対してメンバーアクセスしないで
"""
import random


class _Hoge:
    A: int = 10


class_ = None if random.random() > 0.5 else _Hoge()
_ = class_.A
