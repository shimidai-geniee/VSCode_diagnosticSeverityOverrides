"""
- Diagnostics for missing call to parent class for inherited `__init__` methods.
- super().__init__() を呼びましょう
"""


class Hoge:
    def __init__(self):
        pass
