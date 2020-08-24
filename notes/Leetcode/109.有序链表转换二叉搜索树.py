#
# @lc app=leetcode.cn id=109 lang=python
#
# [109] 有序链表转换二叉搜索树
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def helper(head, tail):
            if head == tail:
                return
            mid = self.findMidNode(head, tail)
            root = TreeNode(mid.val)
            root.left = helper(head, mid)
            root.right = helper(mid.next, tail)
            return root

        return helper(head, None)    

    def findMidNode(self, head, tail):     
        slow, fast = head, head
        while fast != tail and fast.next != tail:
            slow = slow.next
            fast = fast.next.next
        return slow
        
# @lc code=end

