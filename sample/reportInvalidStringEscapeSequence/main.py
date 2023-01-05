"""
- Diagnostics for invalid escape sequences used within string literals. The Python specification indicates that such sequences will generate a syntax error in future versions.
- サポートされていない文字列のエスケープです
"""

import re


_ = re.compile("\[(.*?)\]")
