"""
- Diagnostics for an attempt to access a non-required key within a TypedDict without a check for its presence.
- 必須でないキーの存在する TypedDict では .get() で取得しましょう
"""

from typing_extensions import TypedDict


class _Hoge(TypedDict, total=False):
    key1: int
    key2: str


hoge: _Hoge = {}

_ = hoge["key1"]
