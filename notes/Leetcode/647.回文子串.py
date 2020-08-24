#
# @lc app=leetcode.cn id=647 lang=python
#
# [647] 回文子串
#

# @lc code=start
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        """
        算法：中间拓展
        思路：
            从第i个位置或者第i与i+1个位置开始左右拓展，判断是不是回文串，如果是的话就计数
            可以拓展的中心位置有2n+1个
            所以getCount有两次，一次从i,i拓展，一次从i,i+1拓展
        """
        def getCount(l, r):
            counter = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                counter += 1
                l -= 1
                r += 1
            return counter
        counter = 0
        for i in range(len(s)):
            counter += getCount(i, i)
            counter += getCount(i, i + 1)
        return counter
# @lc code=end

