# print('Hello World')
#
# print('Hello Git')
# print('Hello Git on Pycharm')

import time as t
import random as r

list = [r.randint(0, 10)]* 10
new_list = []

while len(list) > 0:
    small_num = min(list)
    list.remove(small_num)
    new_list.append(small_num)

print(new_list)