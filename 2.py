"""
You are given integers n and m representing a board of size n by m. You also have an unlimited number of 1 by 2 dominos.

Return the maximum number of dominos that can be placed on the board such that they don't overlap and every domino lies entirely within the board.

Example 1
Input     n = 2
          m = 2
Output    2
"""

class Solution:
    def solve(self, n, m):
        t=n*m
        return( t//2)