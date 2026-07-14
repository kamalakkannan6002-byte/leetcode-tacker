# Last updated: 7/14/2026, 2:00:48 PM
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        return len(words[-1])