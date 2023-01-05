"""
- Diagnostics for an attempt to use an Optional type as a context manager (as a parameter to a with statement).
- コンテキストマネージャーが None の可能性があります
"""

import contextlib
import random
from typing import Iterator


@contextlib.contextmanager
def hoge() -> Iterator[float]:
    x = random.random()
    try:
        yield x
    finally:
        print(x)


ctx = hoge() if random.random() < 0.5 else None

with ctx as x:
    pass
