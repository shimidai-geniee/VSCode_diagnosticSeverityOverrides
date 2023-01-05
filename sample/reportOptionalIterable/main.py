"""
- Diagnostics for an attempt to use an Optional type as an iterable value (e.g. within a for statement).
- None に対して反復処理しないで
"""
import random

data = None if random.random() > 0.5 else [1, 2, 3]
_ = [x + 1 for x in data]
