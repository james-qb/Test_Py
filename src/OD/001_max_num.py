#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time    : 2023/6/3 10:09
  @Description:描述
  @Author  : qiubin 
  @File    : 001_max_num.py
  @Software: PyCharm
"""
import time
from collections import Counter


def max_num(num_list, nums=1):
    cnt = Counter(num_list)  # 计数哈希表，记录每一个数字的出现次数
    stack = list()  # 单调递减栈，更大的数字在栈底
    used = {}  # 记录已经入栈的数字，记录每一个数字的出现次数
    for num in num_list:
        # 检查当前字数是否在堆栈中达到要求
        if used.get(num, 0) == nums:
            cnt[num] -= 1
        # 在加入栈底之前，需要进行栈顶元素的检查，
        # 有可能要弹出若干栈顶元素，弹出的条件为：
        # 1.栈不为空；
        # 2.num大于栈顶元素stack[-1]
        # 3.栈顶元素的计数cnt[stack[-1]]大于1（即后面还有其他相同字符可用）
        else:
            while len(stack) > 0 and num > stack[-1] and cnt[stack[-1]] > nums:
                cnt[stack[-1]] -= 1  # 对于栈顶弹出的元素，其计数-1
                used[stack[-1]] -= 1  # 同时在used集合中移除
                stack.pop()  # 栈顶元素弹出
            stack.append(num)
            # 对已经使用的num做统计
            if used.get(num, 0):
                used[num] += 1
            else:
                used[num] = 1
    return stack


# num_lst = "54697785662154564"
# num_lst = "54697785662154564"
# num_lst = "345335568921542348712345669545454646412359456"
# ll = ""
# for i in range(1000):
#     ll += str(random.randint(0, 10))
# num_lst = ll
# print(ll)
num_lst = "130102460501059620169832612774194844532372465694510378767303460"
# num_lst = "543215432154265424697153469"
start = time.time()
result = max_num(num_lst, 3)
print("".join(result))
end = time.time()
print(end - start)
