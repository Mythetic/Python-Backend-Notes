#
# @lc app=leetcode.cn id=376 lang=python
#
# [376] 摆动序列
#

# @lc code=start
class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        up = 1      # 表示当前上升数字的数量
        down = 1    # 表示当前下降数字的数量

        for i in range(1, n):
            if nums[i] > nums[i-1]:
                up = down + 1
            elif nums[i] < nums[i-1]:
                down = up + 1
        
        return max(up, down)
# @lc code=end

