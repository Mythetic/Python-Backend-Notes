#
# @lc app=leetcode.cn id=207 lang=python
#
# [207] 课程表
#

# @lc code=start
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from collections import deque,defaultdict
        graph = defaultdict(list)       # 邻接表
        in_degrees = [0 for _ in range(numCourses)]     # 入度数组
        # 想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]
        # [0,1] 表示 1 在先，0 在后
        # 注意：邻接表存放的是后继 successor 结点的集合
        for x, y in prerequisites:
            graph[y].append(x)
            in_degrees[x] += 1
        # 将入度为 0 的顶点均入队列
        queue = deque([i for i in range(len(in_degrees)) if in_degrees[i] == 0])
        cnt = 0
        while queue:
            top = queue.pop()
            cnt += 1
            # 将入度为0的加入队列
            for successor in graph[top]:
                in_degrees[successor] -= 1
                if in_degrees[successor] == 0:
                    queue.appendleft(successor)
        return cnt == numCourses
# @lc code=end

