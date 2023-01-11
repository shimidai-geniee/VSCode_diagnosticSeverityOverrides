"""
- Diagnostics for 'assert' statement that will provably always assert. This can be indicative of a programming error.
- 常に True となる assert 判定です
"""

assert (1 != 2, "error message")  # Assert expression always evaluates to true
