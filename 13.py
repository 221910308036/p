"""
Given a list of integers nums, find the most frequently occurring element and return the number of occurrences of that element.
For example, given the list [1, 4, 1, 7, 1, 7, 1, 1], return 5 since the the element 1 appears 5 times.
Constraints
	n ≤ 100,000 where n is the length of nums
Example 1
Input
nums = [1, 4, 1, 7, 1, 7, 1, 1]
Output
5
Example 2
Input
nums = [5, 5, 5, 5, 5, 5, 5]
Output
7
Example 3
Input
nums = [1, 2, 3, 4, 5, 6, 7]
Output
1
"""
class Solution:
    def solve(self, nums):
        counter = 0
        nums = nums[0] 
        for i in nums: 
            frequency = nums.count(i) 
            if(frequency> counter): 
                counter = frequency 
                nums = i 
        return frequency
