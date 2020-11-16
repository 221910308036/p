"""
Given an integer n greater than or equal to 0, return the number of 1 bits in n.
Example 1
Input
n = 0
Output
0
Example 2
Input
n = 1
Output
1
Example 3
Input
n = 2
Output
1
Explanation
2 is 10 in binary.
Example 4
Input
n = 3
Output
2
Explanation
3 is 11 in binary.
Example 5
Input
n = 4
Output
1
Explanation
4 is 100 in binary.
"""
class Solution:
    def solve(self, n):
        count = 0
        while (n): 
            count += n & 1
            n >>= 1
        return count

