"""
- Diagnostics for a missing or misnamed “self” parameter in instance methods and “cls” parameter in class methods. Instance methods in metaclasses (classes that derive from “type”) are allowed to use “cls” for instance methods.
- self が抜けている等の問題があります
"""


class Hoge:
    def hoge() -> None:
        pass
