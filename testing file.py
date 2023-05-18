# print('Hello World')
#
# print('Hello Git')
# print('Hello Git on Pycharm')

import time as t

t0 = t.time()


# Bad slow code as an example in the textbook (script 1)
# inefficient

n = 10000
count = 0
for i in range(2,n + 1):
    no_factors_found = True
    f = 2
    while no_factors_found and f < i:
        if i % f == 0:
            no_factors_found = False
        f += 1

    if no_factors_found:
        count += 1

print("# Prime numbers between 2 and", str(n) + ":", count)

t1 = t.time()

print(t1 - t0)


# Faster code (better)
# Does it work? yes
ti =t.time()

n = 10000

still_is_prime = ( n +1)*[ True ]

for i in range (2 , n):
    if still_is_prime [ i ]:
        j = 2* i
        while j <= n :
            still_is_prime [ j ] = False
            j += i

count = sum([1 for v in still_is_prime[2:] if v])

print(" # Prime numbers between 2 and " + str(n) + ":", count)

tf = t.time()

print(tf-ti)

# n = 20
#
# still_is_prime = ( n +1)*[ True ]
#
# for i in range (2 , n ):
#     if still_is_prime [ i ]:
#         j = 2* i
#         while j <= n :
#             still_is_prime [ j ] = False
#             j += i
#
#
# count = sum ([1 for v in still_is_prime [2:] if v ])
#
# print ( " # Prime numbers between 2 and " + str ( n ) + " : " , count )
