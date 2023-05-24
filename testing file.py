# print('Hello World')
#
# print('Hello Git')
# print('Hello Git on Pycharm')
import time
import random as r

list = list()


t1 = time.time()

n = 100000

while n > 0:
    num = r.randint(1,9)
    list.append(num)

    n -= 1


t2 = time.time()

new_list_sorted = sorted(list)
t3 = time.time()

new_list_looped = []

while len(list) > 0:
    small_num = min(list)
    list.remove(small_num)
    new_list_looped.append(small_num)

t4 = time.time()


tl = t2 - t1
tsorted = t3 - t2
tloop = t4 - t3


print(new_list_looped)
print(new_list_sorted)
print('new list made in: ' + str(tl))
print('Sorted in: ' + str(tloop), 'using the while loop')
print('Sorted in: ' + str(tsorted), 'using the the sort method')