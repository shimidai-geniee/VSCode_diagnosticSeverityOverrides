"""
- Diagnostics when “namedtuple” is used rather than “NamedTuple”. The former contains no type information, whereas the latter does.
- namedtuple ではなく NamedTuple を使いましょう
"""
from collections import namedtuple

Hoge = namedtuple("Hoge", ["x", "y"])
