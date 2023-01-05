"""
- Diagnostics for 'isinstance' or 'issubclass' calls where the result is statically determined to be always true or always false. Such calls are often indicative of a programming error.
- 不要な isinstance です
"""
x = 1
if isinstance(x, int):
    print(x)
