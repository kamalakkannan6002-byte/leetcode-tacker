# Last updated: 7/14/2026, 2:00:26 PM
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()     
        words.reverse()        
        return " ".join(words) 


