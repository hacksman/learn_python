#!/usr/bin/env python 
# coding:utf-8
# @Time :10/20/18 17:30

class Listnode(object):

    def __init__(self, val):
        self.val = val
        self.next = None


node1 = Listnode(1)
node2 = Listnode(2)
node3 = Listnode(3)
node4 = Listnode(4)
node5 = Listnode(5)

# class Solution:
#     def removeNthFromEnd(self, head, n):
#         def index(node):
#             if not node:
#                 return 0
#             i = index(node.next) + 1
#             if i > n:
#                 node.next.val = node.val
#             return i
#         index(head)
#         return head.next


# class Solution:
#     def removeNthFromEnd(self, head, n):
#         def remove(head):
#             if not head:
#                 return 0, head
#             i, head.next = remove(head.next)
#             node = (head, head.next)[i + 1 == n]
#             return i+1, node
#         return remove(head)[1]


class Solution:
    def removeNthFromEnd(self, head, n):
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head


if __name__ == '__main__':
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    s = Solution()
    d = s.removeNthFromEnd(node1, 2)