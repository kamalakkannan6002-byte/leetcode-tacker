# Last updated: 7/14/2026, 2:01:25 PM
class Solution:
    def longestCommonPrefix(self, strs):

        prefix = strs[0]

        for s in strs[1:]:

            while not s.startswith(prefix):
                prefix = prefix[:-1]

                if prefix == "":
                    return ""

        return prefix


strs = ["flower", "flow", "flight"]

obj = Solution()
print(obj.longestCommonPrefix(strs))
    