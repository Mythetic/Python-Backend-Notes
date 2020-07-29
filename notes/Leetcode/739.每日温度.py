#
# @lc app=leetcode.cn id=739 lang=python
#
# [739] 每日温度
#

# @lc code=start
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        if not T:
            return []
        n = len(T)
        stack = []
        res  = [0] * n 

        for idx, val in enumerate(T):
            while stack and val > T[stack[-1]]:
                tmp_i = stack.pop()
                res[tmp_i] = idx - tmp_i
            stack.append(idx)
        
        return res

# @lc code=end

