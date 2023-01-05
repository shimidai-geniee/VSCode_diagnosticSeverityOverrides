"""
- Diagnostics for call expressions whose results are not consumed and are not None.
- 戻り値ある関数で意図的に戻り値を使わないなら "_" に入れるべきです
"""


def _x() -> int:
    return 1


_x()
