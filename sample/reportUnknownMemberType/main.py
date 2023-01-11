"""
- Diagnostics for class or instance variables that have an unknown type.
- クラス/インスタンス変数の型が不明です
"""


class _Hoge:
    pass


hoge = _Hoge()

hoge.a  # Type of "a" is unknown [reportUnknownMemberType]
