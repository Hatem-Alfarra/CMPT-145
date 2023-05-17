# print('Hello World')
#
# print('Hello Git')
# print('Hello Git on Pycharm')

n = 100000

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
print((count + 1)- 100000)

# n = 12 # end of range of numbers to check for primes
#
# count = 0
# for i in range (2 , n + 1):
#     no_factors_found = True # assume prime until disproven
#     f = 2
#     # check if i is prime by checking remainders
#     while no_factors_found and f < i :
#         if i % f == 0:
#             no_factors_found = False
#         f += 1
# if no_factors_found:
#     count += 1
#
# print ("# Prime numbers between 2 and " + str (n ) + ":", count )


# n = 10
#
# count = 0
# for potential_prime in range(2, n+1):
#     not_factorable = True
#     potential_comp = 2
#     while not_factorable and potential_comp < potential_prime:
#         if potential_prime % potential_comp == 0:
#             not_factorable = False
#             potential_comp += 1
#     if not_factorable:
#         count += 1
#
# print(count)