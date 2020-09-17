#
# @lc app=leetcode.cn id=491 lang=python
#
# [491] 递增子序列
#

# @lc code=start
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        def backtrace(nums, temp):
            if len(temp)>=2 and temp not in res:
                res.append(temp)
                
            if not nums:
                return

            for i in range(len(nums)):
                # 判断 temp最后一个 是否小于 数组中的想要进来的数
                #就是temp是一个递增数组  进来的数必须大于等于temp 数组最后一个
                if not temp or nums[i]>=temp[-1]:
                    backtrace(nums[i+1:],temp+[nums[i]])
        backtrace(nums,[])
       
        return res



# @lc code=end

