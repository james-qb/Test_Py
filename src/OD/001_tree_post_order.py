#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time    : 2023/7/2 9:43
  @Description:描述
  @Author  : qiubin 
  @File    : 001_tree_post_order.py
  @Software: PyCharm
"""
from collections import deque


# # input_str = "1 2 3 4 5 6 7 8 9"
#
# input_str = "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14"
#
# input_lst = list(map(int, input_str.split()))
# n = len(input_lst)
#
#
# # input_lst = list(map(int, input().split()))
# def find_yezi(input_lst, node, res):
#     left_node = node * 2 + 1
#     if len(input_lst) > left_node:
#         find_yezi(input_lst, left_node, res)
#         right_node = node * 2 + 2
#         if len(input_lst) > right_node:
#             find_yezi(input_lst, right_node, res)
#         res.append(input_lst[node])
#
#
# res = []
# find_yezi(input_lst, 0, res)
# print(res)


class TreeNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None
        self.queue = deque()

    def push(self, value):
        node = TreeNode(value)
        if self.queue:
            if self.queue[0].left is None:
                self.queue[0].left = node
            elif self.queue[0].right is None:
                self.queue[0].right = node
                self.queue.popleft()
        else:
            self.root = node
        self.queue.append(node)

    def post_traversal(self):
        result = []

        def _do_travalsal(node):
            if node is None:
                return None
            else:
                _do_travalsal(node.left)
                _do_travalsal(node.right)
                result.append(node.data)

        _do_travalsal(self.root)
        return result

    def level_traversal(self):
        result = []
        if self.root is None:
            return None
        else:
            queue = [self.root]
        while queue:
            result.append(queue[0].data)
            if queue[0].left:
                queue.append(queue[0].left)
            if queue[0].right:
                queue.append(queue[0].right)
            queue.pop(0)
        return result

    def pre_traversal(self):
        result = []

        def _do_travalsal(node):
            if not node:
                return
            result.append(node.data)
            _do_travalsal(node.left)
            _do_travalsal(node.right)

        _do_travalsal(self.root)
        return result


input_str = "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14"
input_lst = list(map(int, input_str.split()))
n = len(input_lst)
node_list = []
tree = Tree()
for i in range(n):
    if 2 * i + 1 < n:
        node_list.append(input_lst[i])
        tree.push(input_lst[i])
print(tree.post_traversal())
print(tree.level_traversal())
