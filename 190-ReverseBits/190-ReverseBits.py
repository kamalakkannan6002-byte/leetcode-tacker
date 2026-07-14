# Last updated: 7/14/2026, 2:00:24 PM
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        for i in range(32):
            result = (result << 1) | (n & 1)
            n = n >> 1

        return result