#
# @lc app=leetcode.cn id=241 lang=python
#
# [241] 为运算表达式设计优先级
#

# @lc code=start
class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        # 如果只有数字，直接返回
        if input.isdigit():
            return [int(input)]
        
        res = []
        for idx, char in enumerate(input):
            # 1.分解：遇到运算符，计算左右两侧的结果集
            # 2.解决：diffWaysToCompute 递归函数求出子问题的解
            if char in ('+', '-', '*'):
                left = self.diffWaysToCompute(input[:idx])
                right = self.diffWaysToCompute(input[idx+1:])
                # 3.合并：根据运算符合并子问题的解
                for l in left:
                    for r in right:
                        if char == '+':
                            res.append(l+r)
                        elif char == '-':
                            res.append(l-r)
                        elif char == '*':
                            res.append(l*r)
        return res
# @lc code=end

