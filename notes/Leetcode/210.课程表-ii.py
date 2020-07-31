#
# @lc app=leetcode.cn id=210 lang=python
#
# [210] 课程表 II
#

# @lc code=start
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # 拓扑排序
        if not prerequisites:
            return [i for i in range(numCourses)]
        
        indegrees = [0 for _ in range(numCourses)]      # 入度表
        adj = [set() for _ in range(numCourses)]        # 邻接表

        for end, start in prerequisites:
            indegrees[end] += 1
            adj[start].add(end)
        
        from collections import deque
        queue = deque()

        # 将所有入度为0的节点入队
        for i, x in enumerate(indegrees):
            if not x:
                queue.append(i)
        
        res = []

        # BFS
        while queue:
            cur = queue.popleft()
            res.append(cur)

            #  删掉该节点为起始的边
            for neighbor in adj[cur]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
        
        return res if len(res) == numCourses else []
# @lc code=end

