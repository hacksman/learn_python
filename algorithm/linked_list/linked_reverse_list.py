#!/usr/bin/env python 
# coding:utf-8
# @Time :10/21/18 10:21

import copy

class ListNode(object):

    def __init__(self, val):
        self.val = val
        self.next = None


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        def reserve(node):
            if not node.next:
                return [node]

            node_list = reserve(node.next)

            current_node = ListNode(node.val)

            node_list.append(current_node)

            return node_list

        reserve_node = reserve(head)
        for i in range(len(reserve_node)):
            if len(reserve_node) > i+1:
                reserve_node[i].next = reserve_node[i+1]

        return reserve_node[0]



if __name__ == '__main__':
    s = Solution()
    result = s.reverseList(head=node1)
    print(result)
