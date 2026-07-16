# Last updated: 7/16/2026, 12:35:51 PM
1import random
2class Solution:
3    def __init__(self, nums):
4        self.original = nums[:]
5        self.array = nums[:]
6    def reset(self):
7        self.array = self.original[:]
8        return self.array
9    def shuffle(self):
10        shuffled = self.array[:]
11        for i in range(len(shuffled) - 1, 0, -1):
12            j = random.randint(0, i)
13            shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
14        self.array = shuffled
15        return self.array