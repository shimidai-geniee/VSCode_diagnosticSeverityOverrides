"""
- Diagnostics for attempts to redefine variables whose names are all-caps with underscores and numerals.
- 大文字 + _ + 数字 で構成された変数を再定義してます
"""
HOGE_1 = "aiueo"
print(HOGE_1)
HOGE_1 = "hogehoge"
print(HOGE_1)
