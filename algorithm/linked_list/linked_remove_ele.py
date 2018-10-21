#!/usr/bin/env python 
# coding:utf-8
# @Time :10/21/18 15:18


class Listnode(object):

    def __init__(self, val):
        self.val = val
        self.next = None


node1 = Listnode(1)
node2 = Listnode(2)
node3 = Listnode(3)
node4 = Listnode(4)
node5 = Listnode(5)
node6 = Listnode(6)
node6_2 = Listnode(6)

import copy


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        if not head:
            return None

        if not head.next and head.val == val:
            return None

        new_node = []
        while head:
            curr = head
            head = head.next
            curr.next = None
            if curr.val != val:
                new_node.append(curr)

        for i in range(len(new_node)):
            if i < len(new_node) - 1:
                new_node[i].next = new_node[i+1]
        return new_node[0]


if __name__ == '__main__':
    node1.next = node2
    node2.next = node6
    node6.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6_2
    a = node1
    s = Solution()
    b = s.removeElements(a, val=6)

    print(b)
