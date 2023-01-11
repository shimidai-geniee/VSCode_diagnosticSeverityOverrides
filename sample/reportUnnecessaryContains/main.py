"""
- Diagnostics for 'in' operation that is statically determined to be unnecessary. Such operations are sometimes indicative of a programming error.
- 不要な in 句です
"""

from typing_extensions import Literal


def hoge(x: Literal[1, 2, 3]) -> None:
    # Expression will always evaluate to False since the types "Literal[1, 2, 3]" and "Literal[4, 5]" have no overlap [reportUnnecessaryContains]
    if x in (4, 5):
        return

    pass
