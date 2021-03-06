#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# me@nagexiucai.com
# cleanup the shopping trolley.

# ====================题目====================
# 如下订单小票：
'''
Datetime : 2000-01-01 20:00:00
UserID   : 00000001
Goods    : 3
----------------------------------------
Number    Name    Count    Price
03021     苹果    3.0(斤)  2.50(元/斤)
02005     白砂糖  1(包)    8.80(元/包)
07011     香皂    1(块)    4.00(元/块)
----------------------------------------
Coupon: 3
#####
Expire date : 2000-02-01 00:00:00
Discount    : 0.88
#####
Expire date : 2000-02-20 00:00:00
Discount    : -10.00(元)
'''
# 试照例构造小票数据
# 实现结账算法
# 其中优惠券
#    小数表示打折（如0.88即八八折）
#    负数表示抵现（如“-10”即立减十元——不足十元免费）
# 其中包装单位仅限于斤、包、块
#    斤的数量可取精确到“两”的小数
#    包、块均为自然数
# 数据从文件读取（bill.txt）
# 结果输出到文件（payment.txt）
