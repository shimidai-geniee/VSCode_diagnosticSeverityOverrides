"""
- Diagnostics for an attempt to use an Optional type as an operand to a binary or unary operator (like '+', '==', 'or', 'not').
- None に対して不適切な演算子を使わないで
"""

import random

x = random.random()
a = None if x > 0.5 else int(x * 10)
if a > 1:
    print(a)
