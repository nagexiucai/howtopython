#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# me@nagexiucai.com
# utils for human resource.

# 通过Excel另存为CSV文件

# csvpath = "D:\\test\\employees.csv"
# csv = open(csvpath, mode="r") # 文本读
# employees = csv.read() # 一次性读完整个文件
# csv.close() # 读完关闭打开的文件

employees = u'''


姓名,年龄,工号,身份证号,岗位,月薪,入职时间,状态,家庭住址
        张三,27,1001,610582199001010011,研发,10000,2016-09-03,在职,高新区
  
    李四,32,1002,610582199001010012,研发,15000,2018-03-12,在职,未央区
王五,44,1033,610582199001010033,销售,11000,2018-04-11,在职,灞桥区


'''

# 把每个员工的信息切割出来

employees = employees.strip() # 去掉文件开始和末尾可能存在的空行

u'''姓名,年龄,工号,身份证号,岗位,月薪,入职时间,状态,家庭住址
        张三,27,1001,610582199001010011,研发,10000,2016-09-03,在职,高新区
  
    李四,32,1002,610582199001010012,研发,15000,2018-03-12,在职,未央区
王五,44,1033,610582199001010033,销售,11000,2018-04-11,在职,灞桥区'''

lines = employees.split("\n") # 用换行符分隔成由每一行组成的列表

[
    u"姓名,年龄,工号,身份证号,岗位,月薪,入职时间,状态,家庭住址\n",
    u"        张三,27,1001,610582199001010011,研发,10000,2016-09-03,在职,高新区\n",
    u"  \n",
    u"    李四,32,1002,610582199001010012,研发,15000,2018-03-12,在职,未央区\n",
    u"王五,44,1033,610582199001010033,销售,11000,2018-04-11,在职,灞桥区"
]

newlines = []
for line in lines:
    line = line.strip() # 去掉改行两端可能存在的空白
    newlines.append(line)

[
    u"姓名,年龄,工号,身份证号,岗位,月薪,入职时间,状态,家庭住址",
    u"张三,27,1001,610582199001010011,研发,10000,2016-09-03,在职,高新区",
    u"",
    u"李四,32,1002,610582199001010012,研发,15000,2018-03-12,在职,未央区",
    u"王五,44,1033,610582199001010033,销售,11000,2018-04-11,在职,灞桥区"
]

# 列表解析
# newlines = [line.strip() for line in lines] # 把列表中每一行两端可能存在的空白去除

newnewlines = []
for line in newlines:
    if line: # 默认调用bool函数
        newnewlines.append(line)

[
    u"姓名,年龄,工号,身份证号,岗位,月薪,入职时间,状态,家庭住址",
    u"张三,27,1001,610582199001010011,研发,10000,2016-09-03,在职,高新区",
    u"李四,32,1002,610582199001010012,研发,15000,2018-03-12,在职,未央区",
    u"王五,44,1033,610582199001010033,销售,11000,2018-04-11,在职,灞桥区"
]

# 采用内建的filter函数
# newnewlines = filter(bool, newlines) # 过滤掉可能存在的空行

titles = None
data = []
n = 0
for line in newnewlines:
    items = line.split(",")
    if n == 0: # 代表第一行
        titles = items
    else:
        # 笨办法把两个序列相同索引位置上的值对应起来
        info = {}
        for i in range(len(titles)):
            info[titles[i]] = items[i]
        data.append(info)
    n += 1

def show(data):
    for d in data:
        print "-----------"
        for k, v in d.items():
            print k, ":", v

# show(data)

# 至此，已将文件信息建模，形成规范的数据结构。

# 数据分析

## 排序：月薪
def sort_by_salary(data):
    # 用冒泡排序算法
    for i in range(len(data)):
        for j in range(len(data)):
            if int(data[i][u"月薪"]) > int(data[j][u"月薪"]):
                temp = data[i]
                data[i] = data[j]
                data[j] = temp

sort_by_salary(data)
show(data)

## 统计：男女比例、年龄层次、学历

# 图形展示
