# Last updated: 7/14/2026, 2:01:16 PM
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:
            if ch in pairs.values():  
                stack.append(ch)
            else:  
                if not stack or stack.pop() != pairs[ch]:
                    return False

        return len(stack) == 0