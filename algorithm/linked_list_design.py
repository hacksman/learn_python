#!/usr/bin/env python 
# coding:utf-8
# @Time :10/18/18 09:28

"""
 资料来源：
    https://leetcode.com/problems/design-linked-list/discuss/178109/Python-a-simple-and-fast-(91)-solution
"""

class LinkNode(object):
    def __init__(self, val):
        self.val = val
        self.prev = self.next = None


class MyLinkedList(object):

    # 初始化状态，有哨兵节点
    def __init__(self):
        self.val = None
        self.head = LinkNode(None)
        self.tail = LinkNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index):
        if self._in_range(index, 0, self.size - 1):
            return self._go_to_node(index).val
        return -1

    def addAtHead(self, val):
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index, val):
        if self._in_range(index, 0, self.size):
            new_node = LinkNode(val)
            curr_node = self._go_to_node(index)
            new_node.next = curr_node
            new_node.prev = curr_node.prev
            curr_node.prev.next = new_node
            curr_node.prev = new_node
            self.size += 1

    def deleteAtIndex(self, index):
        if self._in_range(index, 0, self.size - 1):
            current_node = self._go_to_node(index)
            current_node.prev.next = current_node.next
            current_node.next.prev = current_node.prev
            self.size -= 1

    def _in_range(self, index, start, end):
        return start <= index <= end

    def _go_to_node(self, index):
        if index < self.size // 2:
            curr = self.head
            for _ in range(-1, index):
                curr = curr.next
        else:
            # go back
            curr = self.tail
            for _ in range(self.size, index, -1):
                curr = curr.prev
        return curr


if __name__ == '__main__':
    my_link_list = MyLinkedList()       # 初始化链表
    my_link_list.addAtHead(1)           # 在头部添加元素
    my_link_list.addAtTail(2)           # 在尾部添加元素
    my_link_list.addAtIndex(1, 3)       # 在index为1的地方添加元素
    my_link_list.get(1)                 # 获取索引为1处的元素
    my_link_list.deleteAtIndex(1)       # 删除索引为1处的元素
    my_link_list.get(1)                 # 获取索引为1处的元素
