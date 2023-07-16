#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time    : 2023/7/2 10:26
  @Description:描述
  @Author  : qiubin 
  @File    : 013_longest_shunzi.py
  @Software: PyCharm
"""
# hand_porker = "3-3-3-3-4-4-5-5-6-7-8-9-10-J-Q-K-A"
# out_porker = "4-5-6-7-8-8-8"

hand_porker = "3-3-3-3-7-7-7-7"
out_porker = "2-2-2-2"
# hand_porker_lst = list(input().split('-'))
# out_porker_lst = list(input().split('-'))
hand_porker_lst = list(hand_porker.split('-'))
out_porker_lst = list(out_porker.split('-'))
print(hand_porker_lst, out_porker_lst)
porker_str_lst = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2', 'B', 'C']
count_dcit = {}
for i in range(len(porker_str_lst)):
    if i < 13:
        count_dcit[porker_str_lst[i]] = 4
    else:
        count_dcit[porker_str_lst[i]] = 1
for porker_str in hand_porker_lst + out_porker_lst:
    count_dcit[porker_str] -= 1
print(count_dcit)

porker_count = [0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 1]
pork_to_num_dict = {
    '3': 3, '4': 4, '5': 5, '6': 6,
    '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 11, 'Q': 12, 'K': 13, 'A': 14,
    '2': 15, 'Y': 16, 'Z': 17,
}
num_to_porker_dict = {}
for k, v in pork_to_num_dict.items():
    num_to_porker_dict[v] = k
for pai in hand_porker_lst + out_porker_lst:
    porker_count[pork_to_num_dict[pai]] -= 1

stack = []
start = pork_to_num_dict['3']
end = pork_to_num_dict['3']
last = pork_to_num_dict['A']

# start = count_dcit['3']
# end = count_dcit['3']
# last = count_dcit['A']

while 3 <= start <= last - 4 and 3 <= end <= last:
    if porker_count[start] == 0:
        start += 1
        end = start + 1
        continue
    if porker_count[end] > 0:
        if end - start >= 4:
            while end + 1 < last and porker_count[end + 1] > 0:
                end += 1
            if not stack:
                stack = [start, end]
            else:
                if end - start >= stack[1] - stack[0]:
                    stack = [start, end]
        end += 1
    else:
        start = end
if not stack:
    result = "NO-CHAin"
else:
    result = "-".join([num_to_porker_dict[i] for i in range(stack[0], stack[1] + 1)])
print(result)
