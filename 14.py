"""
You’re given a string containing letters of three types, R, B, and ..
R represents your current position, B represents a blocked position, and . represents an empty position. In one step, you can move to any adjacent position to your current position, as long as it is empty. Can you reach either the leftmost position or the rightmost position?
Return true if you can reach either the leftmost or the rightmost position, or false if you cannot.
Example 1
Input
s = "......B....R.............."
Output
True
Explanation
We can reach the rightmost position since it's not blocked.
Example 2
Input
s = "B...B...R........BBBB"
Output
False
Explanation
We can't reach either side since they're both blocked.

"""
class Solution:
    def solve(self, s):
        x = s.find('R')
        return not 'B' in s[:x] or not 'B' in s[x:]

