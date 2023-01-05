"""
- Diagnostics for '==' and '!=' comparisons that are statically determined to be unnecessary. Such calls are sometimes indicative of a programming error.
- 不要な比較です
"""
a = None
if a == 1:
    print(1)
