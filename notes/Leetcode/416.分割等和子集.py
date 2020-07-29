#
# @lc app=leetcode.cn id=416 lang=python
#
# [416] 分割等和子集
#

# @lc code=start
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 01背包 
        if not nums:
            return False
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        
        dp = [False] * (target+1)
        dp[0] = True

        for num in nums:
            for i in range(target, num-1, -1):
                if dp[i-num]:
                    dp[i] = True
        
        return dp[-1]

# @lc code=end

