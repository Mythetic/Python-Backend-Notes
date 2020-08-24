#
# @lc app=leetcode.cn id=133 lang=python
#
# [133] 克隆图
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        # DFS 借助dict判断是否遍历
        lookup = {}

        def dfs(node):
            if not node:
                return
            if node in lookup:
                return lookup[node]
            clone = Node(node.val, [])
            lookup[node] = clone
            for n in node.neighbors:
                clone.neighbors.append(dfs(n))
            return clone
        
        # BFS
        lookup = {}
        from collections import deque
        def bfs(node):
            if not node:
                return
            clone = Node(node.val, [])
            lookup[node] = clone
            while queue:
                tmp = queue.popleft()
                for n in tmp.neighbors:
                    if n not in lookup:
                        lookup[n] = Node(n.val, [])
                        queue.append(n)
                    lookup[tmp].neighbors.append(lookup[n])
            return clone


        return dfs(node)
# @lc code=end

