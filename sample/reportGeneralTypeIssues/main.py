"""
- Diagnostics for general type inconsistencies, unsupported operations, argument/parameter mismatches, etc. Covers all of the basic type-checking rules not covered by other rules. Does not include syntax errors.
- 一般的な型不整合。他のオプションに該当しないものが色々。
"""


def _x(x: int) -> int:
    return x * 2


_x()  # 引数がないとか
