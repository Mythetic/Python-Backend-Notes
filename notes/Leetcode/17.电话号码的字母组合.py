#
# @lc app=leetcode.cn id=17 lang=python
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []
        if not digits:
            return []
        phone = {'2': ['a', 'b', 'c'],
                    '3': ['d', 'e', 'f'],
                    '4': ['g', 'h', 'i'],
                    '5': ['j', 'k', 'l'],
                    '6': ['m', 'n', 'o'],
                    '7': ['p', 'q', 'r', 's'],
                    '8': ['t', 'u', 'v'],
                    '9': ['w', 'x', 'y', 'z']}

        def backtrace(tmp, nextdigits):
            if len(nextdigits) == 0:
                res.append(tmp)
                return
            for c in phone[nextdigits[0]]:
                backtrace(tmp+c, nextdigits[1:])
        backtrace("", digits)
        return res
# @lc code=end

