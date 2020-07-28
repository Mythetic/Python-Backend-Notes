#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        if not nums or k < 0 or k > n:
            return []

        res = []
        from collections import deque
        queue = deque()

        for i in range(n):
            if queue and i-queue[0] >= k:
                queue.popleft()
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
            queue.append(i)
            if i >= k-1:
                res.append(nums[queue[0]])

        return res

# @lc code=end

