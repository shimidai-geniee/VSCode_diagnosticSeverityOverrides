"""
- Diagnostics for variables that have an unknown type..
- 変数の型情報が不明です
"""
x = any()  # type: ignore

y = x

del y
