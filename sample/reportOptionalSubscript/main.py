"""
- Diagnostics for an attempt to subscript (index) a variable with an Optional type.
- None に対してキーアクセスしないで
"""
import random


data = None if random.random() > 0.5 else {"key": 1}
data["key"]
