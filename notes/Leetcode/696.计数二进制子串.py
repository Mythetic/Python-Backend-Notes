#
# @lc app=leetcode.cn id=696 lang=python
#
# [696] 计数二进制子串
#

# @lc code=start
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 统计相邻的连续字符的个数，两者取最小值，累加即为结果
        ptr, last, res = 0, 0, 0
        n = len(s)

        while ptr < n:
            cnt = 0
            c = s[ptr]
            while ptr < n and s[ptr] == c:
                cnt += 1
                ptr += 1
            res += min(last, cnt)
            last = cnt

        return res
# @lc code=end

