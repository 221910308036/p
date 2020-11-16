"""
Given three numbers, a, b, and c, return their product, but if any two numbers are the same, they do not count.
Example 1
Input
a = 2
b = 3
c = 4
Output
24
Explanation
All three numbers are unique so their product is 2 * 3 * 4 = 24
Example 2
Input
a = 3
b = 3
c = 5
Output
5
Explanation
There's two 3s so the product is 5
Example 3
Input
a = 3
b = 3
c = 3
Output
1
Explanation
All three numbers are the same, so they don't count toward the product.

"""
class Solution:
    def solve(self, a, b, c):
        product = 0
        if a == b == c:
            product = 1
        elif a == b:
            product = c
        elif a == c:
            product = b
        elif b == c:
            product = a
        else:
            product = a * b * c
        return product
