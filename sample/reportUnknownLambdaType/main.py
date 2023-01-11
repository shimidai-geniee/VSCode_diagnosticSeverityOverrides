"""
- Diagnostics for input or return parameters for lambdas that have an unknown type.
- lambda 式の引数、戻り値の型が不明です
"""

from typing import Callable


f: Callable  # type: ignore


_ = map(  # type: ignore
    lambda x: f(x),  # Return type of lambda is unknown [portUnknownLambdaType]
    [1, 2, 3],
)
