# -*- coding: utf-8 -*-
# @Time : 2023/1/12 15:42
# @Author : zhoufan
# @Email : 13952047994@163.com
# @File : zidingyichangdu.py
# @Project : geektime_0-master
import random


def ran(num):
    base_str = '1234567890qwertyuiopasdfghjklzxcvbnm_!@#$%^&*()_+><?{}|[]QAZWSXEDCRFVTGBYHNUJMIK<LOP:>'
    str1 = ''.join(random.choices(base_str,k=num))
    return str1


print(ran(180))
