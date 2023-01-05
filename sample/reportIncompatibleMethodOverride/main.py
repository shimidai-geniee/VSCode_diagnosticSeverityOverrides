"""
- Diagnostics for methods that override a method of the same name in a base class in an incompatible manner (wrong number of parameters, incompatible parameter types, or incompatible return type).
- クラスメソッドのオーバーライドで定義が変わってます
"""


class ClassA:
    def hoge(self, x: int) -> None:
        pass


class ClassB(ClassA):
    def hoge(self, x: str) -> None:
        pass
