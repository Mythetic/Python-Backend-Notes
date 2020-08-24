#
# @lc app=leetcode.cn id=20 lang=python
#
# [20] 有效的括号
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        
        lookup = {
            ")" : "(",
            "}" : "{",
            "]" : "[",
        }

        stack = []

        for c in s:
            if not stack:
                stack.append(c)
            elif c in lookup:
                if stack[-1] == lookup[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack
# @lc code=end

