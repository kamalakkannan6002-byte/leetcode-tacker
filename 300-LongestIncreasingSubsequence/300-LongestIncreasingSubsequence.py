# Last updated: 7/14/2026, 2:00:12 PM
from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        tails = []

        for num in nums:
            pos = bisect_left(tails, num)

            if pos == len(tails):
                tails.append(num)
            else:
                tails[pos] = num

        return len(tails)