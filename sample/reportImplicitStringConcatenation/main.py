"""
- Diagnostics for two or more string literals that follow each other, indicating an implicit concatenation. This is considered a bad practice and often masks bugs such as missing commas.
- 暗黙の文字列結合はダメです
"""
_ = "aiu" "eo"
