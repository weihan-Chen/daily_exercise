'''
Author: weihan-Chen
Github: https://github.com/weihan-Chen
Date: 2021-06-23 16:11:19
LastEditors: weihan-Chen
LastEditTime: 2021-06-23 16:25:10
Description: 
'''
import random
import math

N = 10000000
count = 0
i = 0
while i < N:
    number = random.uniform(0, 10)
    if number < math.pi:
        count = count + 1
    i = i + 1
print(count / N * 10)
