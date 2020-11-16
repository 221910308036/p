"""
Given a string s, remove all “y” and “xz” in the string in one iteration.
Example 1
Input
s = "xyxyxz"
Output
"xx"
Example 2
Input
s = "xyz"
Output
"xz"
Explanation
Note only the "y" was removed.

"""
class Solution:
    def solve(self, s):
        return s.replace("xz","").replace("y","")


