#
# @lc app=leetcode.cn id=91 lang=python
#
# [91] 解码方法
#

# @lc code=start
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == "0":   
            return 0
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, n+1):
            # 注意处理"0"的情况
            if s[i-1] == "0":
                if s[i-2] in ("1", "2"):
                    dp[i] = dp[i-2]
                else:
                    return 0
            elif s[i-2] == "1" or (s[i-2] == "2" and int(s[i-1]) <= 6):
                dp[i] = dp[i-2] + dp[i-1]
            else:
                dp[i] = dp[i-1]
        
        return dp[-1]

# @lc code=end

