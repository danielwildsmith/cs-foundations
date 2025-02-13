# Bit Manipulation, Dynamic Programming
# https://leetcode.com/problems/counting-bits/
# 

from typing import List

class Solution:
    # Brute Force. O(n log_2 n) since shifting right each time is equivalent to dividing by 2
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)

        for i in range(n + 1):
            num = i
            while num > 0:
                if num & 1 == 1:
                    res[i] += 1
                num = num >> 1
        
        return res
    
    # 0: 0000
    # 1: 0001
    # 2: 0010
    # 3: 0011
    # 4: 0100
    # 5: 0101
    # 6: 0110
    # 7: 0111
    # 8: 1000

    # Repeated work! At 5, after the most significant bit, we have already found the number of bits in 001.
    # At 8, we encounter a new significant bit. Everything to the right is reset. Where to find the previous computation?
    # In a cache! Look back by an offset of 8. 
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1

        for num in range(1, n + 1):
            if offset * 2 == num:
                offset = num

            dp[num] = 1 + dp[num - offset]

        return dp