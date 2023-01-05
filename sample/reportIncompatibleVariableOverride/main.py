"""
- Diagnostics for overrides in subclasses that redefine a variable in an incompatible way.
- クラス変数のオーバーライドで定義が変わってます
"""


class ClassA:
    X: int = 1


class ClassB(ClassA):
    X: str = "1"
