# Last updated: 7/16/2026, 12:37:22 PM
1class Solution:
2    def searchRange(self, nums, target):
3        first = -1
4        last = -1
5
6        left = 0
7        right = len(nums) - 1
8
9        while left <= right:
10            mid = (left + right) // 2
11
12            if nums[mid] == target:
13                first = mid
14                right = mid - 1
15            elif nums[mid] < target:
16                left = mid + 1
17            else:
18                right = mid - 1
19
20        left = 0
21        right = len(nums) - 1
22
23        while left <= right:
24            mid = (left + right) // 2
25
26            if nums[mid] == target:
27                last = mid
28                left = mid + 1
29            elif nums[mid] < target:
30                left = mid + 1
31            else:
32                right = mid - 1
33
34        return [first, last]