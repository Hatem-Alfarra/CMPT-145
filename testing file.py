# print('Hello World')
#
# print('Hello Git')
# print('Hello Git on Pycharm')

import time as t
import random as r


list = list()

n = 10

while n > 0:
    num = r.randint(1,9)
    list.append(num)

    n -= 1


new_list = []

while len(list) > 0:
    small_num = min(list)
    list.remove(small_num)
    new_list.append(small_num)

print(new_list)