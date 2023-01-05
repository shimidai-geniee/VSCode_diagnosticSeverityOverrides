"""
- Diagnostics for instance variables that are not declared or initialized within class body or `__init__` method.
- クラス変数や __init__ で定義していない変数を新たに使ってます
"""


class Hoge:
    def hoge(self) -> None:
        self.x = 1
