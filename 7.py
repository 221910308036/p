"""
Given a string s containing brackets ( and ), return the minimum number of brackets that can be inserted so that the brackets are balanced.
Constraints
	n ≤ 100,000 where n is the length of s
Example 1
Input
s = ")))(("
Output
5
Explanation
We can insert ((( to the front and )) to the end
"""
class Solution:
    def solve(self, s):
        bal=0
        ans=0
        for i in range(0,len(s)): 
            if(s[i]=='('): 
                bal+=1
            else: 
                bal+=-1
            if(bal==-1): 
                ans+=1
                bal+=1
        return bal+ans
