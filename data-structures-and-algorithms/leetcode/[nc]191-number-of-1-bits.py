# Bit Manipulation
# https://leetcode.com/problems/number-of-1-bits/description/
# https://www.youtube.com/watch?v=5Km3utixwZs&t=1s

# & operand lets you check the first bit, whether its 1 or 0
# e.g. 1101 
#      0001
# =    0001
# If there is a 1 at the first bit, it will be 1. Else, 0.

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n > 0:
            if n & 1 == 1:
                res += 1
            n = n >> 1

        return res