"""
- Diagnostics for function calls within a default value initialization expression. Such calls can mask expensive operations that are performed at module initialization time.
- デフォルト値指定が関数になってます
"""
import random


def _x(x: float = random.random()) -> float:
    return x


del _x
