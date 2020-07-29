#
# @lc app=leetcode.cn id=503 lang=python
#
# [503] 下一个更大元素 II
#

# @lc code=start
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        n = len(nums)
        stack = []
        res = [-1] * n

        for i in range(2*n):
            num = nums[i % n]
            while stack and num > nums[stack[-1]]:
                tmp_i = stack.pop()
                res[tmp_i] = num
            if i < n:
                stack.append(i)
        
        return res

# @lc code=end

