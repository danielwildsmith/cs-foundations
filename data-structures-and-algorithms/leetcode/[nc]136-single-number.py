# Bit Manipulation
# https://leetcode.com/problems/single-number/description/
# https://youtu.be/qMPX1AOa83k?feature=shared

# the XOR operation is associative and commutative. That means a ^ (b ^ c) = (a ^ b) ^ c, and a ^ b = b ^ a. 
# From these two properties, we can see that ((((4 ^ 1 ) ^ 2 ) ^ 1 ) ^ 2 ) = (2 ^ 2) ^ (1 ^ 1) ^ 4. 
# The left hand side of this equation is what the solution code is effectively doing.  
# On the right hand side, we can take the basic XOR operation principles discussed in the video to see that it equals 0 ^ 0 ^ 4 = 0 ^ 4. 
# Since n ^ 0 = n, then we know that the answer is 4.

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res = num ^ res
        return res
