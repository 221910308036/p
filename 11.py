"""
Given a string s, eliminate consecutive duplicate characters from the string and return it.
That is, if a list contains repeated characters, they should be replaced with a single copy of the character. The order of the elements should not be changed.
Constraints
	n ≤ 100,000 where n is the length of s
Example 1
Input
s = "aaaaaabbbccccaaaaddf"
Output
"abcadf"
Example 2
Input
s = "a"
Output
"a"
"""
class Solution:
    def solve(self, s):
        seen = s[0]
        ans = s[0]
        for i in s[1:]:
            if i != seen:
                ans += i
                seen = i
        return ans
