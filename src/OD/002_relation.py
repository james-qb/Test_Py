#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time    : 2023/6/4 13:39
  @Description:描述
  @Author  : qiubin 
  @File    : 002_relation.py
  @Software: PyCharm
"""

"""题目描述：
当前IT部门支撑了子公司颗粒化业务，该部门需要实现为子公司快速开租建站的能力，建站是指在一个全新的环境部署一套IT服务。每个站点开站会由一系列部署任务项构成，每个任务项部署完成时间都是固定和相等的，设为1。部署任务项之间可能存在依赖，假如任务2依赖任务1，那么等任务1部署完，任务2才能部署。任务有多个依赖任务则需要等所有依赖任务都部署完该任务才能部署。没有依赖的任务可以并行部署，优秀的员工们会做到完全并行无等待的部署。给定一个站点部署任务项和它们之间的依赖关系，请给出一个站点的最短开站时间。
输入描述：
第一行是任务数taskNum,第二行是任务的依赖关系数relationsNum
接下来 relationsNum 行，每行包含两个id，描述一个依赖关系，格式为：IDi IDj，表示部署任务i部署完成了，部署任务j才能部署，IDi 和 IDj 值的范围为：[0, taskNum)
注：输入保证部署任务之间的依赖不会存在环。
输出描述：
一个整数，表示一个站点的最短开站时间。
补充说明：
1<taskNum<=100
1=<relationsNum<=5000
 收起
示例1
输入：
5
5
0 4
1 2
1 3
2 3
2 4
输出：
3
说明：
有5个部署任务项，5个依赖关系，如下图所示。我们可以先同时部署任务项0和任务项1，然后部署任务项2，最后同时部署任务项3和任务项4。最短开站时间为3。

示例2
输入：
5
3
0 3
0 4
1 3
输出：
2
说明：
有5个部署任务项，3个依赖关系，如下图所示。我们可以先同时部署任务项0，任务项1，任务项2。然后再同时部署任务项3和任务项4。最短开站时间为2。
"""

tasknum, relationsNum = int(input()), int(input())
relamatrix = []
for i in range(relationsNum):
    relamatrix.append(list(map(int, input().split(" "))))
rear = {}
st = [0 for _ in range(tasknum)]
s = []
atime = 1

for rela in relamatrix:
    x, y = rela
    if x not in rear.keys():
        rear[x] = [y]
    else:
        rear[x].append(y)
    st[y] = st[y] + 1

for i in range(tasknum):
    if st[i] == 0:
        s.append((i, atime))

while len(s) > 0:
    x, y = s.pop(0)
    if rear.get(x) is not None and len(rear[x]) > 0:
        for i in rear[x]:
            st[i] -= 1
            if st[i] == 0:
                atime = y + 1
                s.append((i, atime))
print(atime)
