# Leetcode 347 - Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for num in nums:
            map[num] = map.get(num,0) + 1

        sorted_map = sorted(map.items(), key=lambda x: x[1], reverse=True)

        return [x[0] for x in sorted_map[:k]]



# using bucket sort
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = count.get(n,0) + 1
        
        for key, value in count.items():
            freq[value].append(key)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return res