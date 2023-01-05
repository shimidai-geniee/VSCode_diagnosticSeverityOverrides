"""
- Diagnostics for 'cast' calls that are statically determined to be unnecessary. Such calls are sometimes indicative of a programming error.
- 不要な cast です
"""
from typing import cast


class _Hoge:
    pass


hoge = _Hoge()
_ = cast(_Hoge, hoge)
