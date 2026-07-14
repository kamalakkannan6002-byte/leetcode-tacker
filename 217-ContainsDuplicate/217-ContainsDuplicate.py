# Last updated: 7/14/2026, 2:00:17 PM
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums)) 
        