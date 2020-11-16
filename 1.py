"""

Given an integer n, return whether it is equal to the sum of its own digits raised to the power of the number of digits.

Example 1
Input       n = 153
Output     True
Explanation       153 = 1 ** 3 + 5 ** 3 + 3 ** 3

"""


class Solution:
    def solve(self, n):
        return n==sum([int(x)** len(str(n)) for x in str(n)])
