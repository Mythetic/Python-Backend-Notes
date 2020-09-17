#
# @lc app=leetcode.cn id=347 lang=python
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 桶排序
        if not nums or k < 1:
            return []
        
        res = []
        from collections import Counter
        c = Counter(nums)
        buckets = [[] for _ in  range(len(nums) + 1)]

        for x, y in c.items():
            buckets[y].append(x)
        
        for i in range(len(nums), -1, -1):
            if len(res) >= k:
                break
            
            res.extend(buckets[i])
        
        return res[:k]
# @lc code=end

