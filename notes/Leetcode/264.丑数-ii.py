#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n):
        i2 = i3 = i5 = 0
        dp = [1] * n
        for i in range(1, n):
            minVal = min(2*dp[i2], 3*dp[i3], 5*dp[i5])
            dp[i] = minVal
            if minVal == 2*dp[i2]:
                i2 += 1
            if minVal == 3*dp[i3]:
                i3 += 1
            if minVal == 5*dp[i5]:
                i5 += 1
        return dp[-1]
# @lc code=end

