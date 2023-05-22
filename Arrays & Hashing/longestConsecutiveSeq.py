# Leetcode 128 -  Longest Consecutive Sequence

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n-1) not in numSet:
                length = 0 
                while (n+length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest