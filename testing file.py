# print('Hello World')
#
# print('Hello Git')
# print('Hello Git on Pycharm')

list = [2,3,1,9,5,4,8,7,0]
new_list = []

while len(list) > 0:
    small_num = min(list)
    list.remove(small_num)
    new_list.append(small_num)

print(new_list)