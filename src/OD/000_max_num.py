#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time    : 2023/6/3 10:09
  @Description:描述
  @Author  : qiubin 
  @File    : 000_max_num.py
  @Software: PyCharm
"""
import time
from collections import Counter, defaultdict


def max_num(num_list, nums=1):
    cnt = Counter(num_list)  # 计数哈希表，记录可使用数字的出现次数
    stack = list()  # 单调递减栈，更大的数字在栈底
    used = defaultdict(int)  # 记录已经入栈的数字，记录每一个数字的出现次数
    for num in num_list:
        # 检查当前字数是否在堆栈中达到要求
        if used[num] == nums:
            cnt[num] -= 1
        # 在加入栈底之前，需要进行栈顶元素的检查，
        # 有可能要弹出若干栈顶元素，弹出的条件为：
        # 1.栈不为空；
        # 2.num大于栈顶元素stack[-1]
        # 3.栈顶元素的计数cnt[stack[-1]]大于1（即后面还有其他相同字符可用）
        else:
            while len(stack) > 0:
                if num > stack[-1] and cnt[stack[-1]] + used[stack[-1]] - 1 >= nums:
                    used[stack[-1]] -= 1  # 同时在used集合中移除
                    stack.pop()  # 栈顶元素弹出
                else:
                    break
            stack.append(num)
            used[num] += 1
            cnt[num] -= 1
    return stack


# num_lst = "54697785662154564"
# num_lst = "54697785662154564"
# num_lst = "345335568921542348712345669545454646412359456"
# ll = ""
# for i in range(1000):
#     ll += str(random.randint(0, 10))
# num_lst = ll
# print(ll)
# num_lst = "130102460501059620169832612774194844532372465694510378767303460"
num_lst = "54697785662154564"
start = time.time()
result = max_num(num_lst, 2)
print("".join(result))
end = time.time()
print(end - start)
