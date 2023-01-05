"""
- Diagnostics for incorrect usage of private or protected variables or functions. Protected class members begin with a single underscore _ and can be accessed only by subclasses. Private class members begin with a double underscore but do not end in a double underscore and can be accessed only within the declaring class. Variables and functions declared outside of a class are considered private if their names start with either a single or double underscore, and they cannot be accessed outside of the declaring module.
- プライベートな変数/関数を使ってます
"""


class _Hoge:
    def _hoge(self) -> int:
        return 1


hoge = _Hoge()
_ = hoge._hoge()
