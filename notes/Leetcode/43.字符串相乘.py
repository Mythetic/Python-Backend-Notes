#
# @lc app=leetcode.cn id=43 lang=python
#
# [43] 字符串相乘
#

# @lc code=start
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        k1, k2 = len(num1), len(num2)
        total = ""
        res = [0] * (k1 + k2)   # 存储结果
        for i in range(k1-1, -1, -1):
            n1 = int(num1[i])
            for j in range(k2-1, -1, -1):
                n2 = int(num2[j])
                sum = res[i+j+1] + n1*n2
                res[i+j+1] = sum % 10
                res[i+j] += sum // 10
        for i in range(len(res)):
            if i==0 and res[i] == 0:    # 判断第一位是否为0
                continue
            total = "%s%s" %(total, res[i])
        return total
# @lc code=end

