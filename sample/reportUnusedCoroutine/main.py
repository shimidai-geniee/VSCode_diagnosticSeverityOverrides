"""
- Diagnostics for call expressions that return a Coroutine and whose results are not consumed.
- コルーチンの戻り値が使われていません
"""


async def _fuga() -> int:
    return 1


async def hoge():
    await _fuga()
