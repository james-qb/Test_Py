#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time    : 2023/7/2 11:16
  @Description:描述
  @Author  : qiubin 
  @File    : alibaba_iv.py
  @Software: PyCharm
"""
num_str = "2,6,5,2,1,1,4,7,0,-1"
num_lst = list(map(int, num_str.split(',')))
n = len(num_lst)
print(num_lst)


# 方法一 栈的方式
def find_next_big(num_lst, stack, res):
    for index, value in enumerate(num_lst):
        while True:
            if stack:
                p_value, p_index = stack[-1]
                if value > p_value:
                    res[p_index] = value
                    stack.pop()
                else:
                    stack.append([value, index])
                    break
            else:
                stack.append([value, index])
                break


stack = []
res = [-1] * n

find_next_big(num_lst, stack, res)
if len(stack) != 1:
    find_next_big(num_lst, stack, res)
print(",".join(map(str, res)))

# 第二种放方法，通过n+i,然后取模的方式
# n = len(num_lst)
# stack = [-1] * n
# for i in range(n):
#     for j in range(i + 1, n + i):
#         k = j % n
#         if num_lst[k] > num_lst[i]:
#             stack[i] = num_lst[k]
#             break
# print(",".join(map(str, stack)))

# 方法三 通过for...else的方式循环查找
# n = len(num_lst)
# stack = [-1] * n
# for i in range(n):
#     for j in range(i + 1, n):
#         if num_lst[k] > num_lst[i]:
#             stack[i] = num_lst[k]
#             break
#     else:
#         for j in range(0, i):
#             if num_lst[j] > num_lst[i]:
#                 stack[i] = num_lst[j]
#                 break
# print(",".join(map(str, stack)))
# n = len(num_lst)
# stack = [-1] * n
# start = 0
# end = 1
# while start < n and start < end < start + n:
#     k = end % n
#     if num_lst[k] > num_lst[start]:
#         stack[start] = num_lst[k]
#         start += 1
#         end = start + 1
#     else:
#         if end == start + n - 1:
#             start += 1
#             end = start + 1
#         else:
#             end += 1
# print(",".join(map(str, stack)))
