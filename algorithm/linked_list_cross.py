#!/usr/bin/env python 
# coding:utf-8
# @Time :10/20/18 14:47

"""
 资料来源：
    https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49798/Concise-python-code-with-comments?page=2
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# a1 = ListNode('a1')
# a2 = ListNode('a2')
# b1 = ListNode('b1')
# b2 = ListNode('b2')
# b3 = ListNode('b3')
c1 = ListNode('c1')
c2 = ListNode('c2')
# c3 = ListNode('c3')

# a1.next = a2
# a2.next = c1
c1.next = c2
# c2.next = c3

# b1.next = b2
# b2.next = b3
# b3.next = c1


class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None

        pa = headA # 2 pointers
        pb = headB

        while pa is not pb:
            # if either pointer hits the end, switch head and continue the second traversal,
            # if not hit the end, just move on to next
            pa = headB if pa is None else pa.next
            # print pa
            pb = headA if pb is None else pb.next
            # print pb

        return pa

if __name__ == '__main__':
    node_cross_check = Solution()
    result = node_cross_check.getIntersectionNode(c1, c2)
    print(result)

"""
    如果以 head = head.next 这种方式在for循环中移动链表赋值，则意味着每次都在删除前面的一个节点 
"""