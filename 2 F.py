n = int(input())
num = list(map(int, input().split()))

pref =  [0] * (n-1)
s = 0
for i in  range(0, n-1):
    pref[i]= num[i] * num[i+1]
for i in range(len(pref)):
    s += pref[i] * num[i]

print(pref)
print(s)




# from itertools import combinations
# import math
#
# n = int(input())
# num = map(int, input().split())
# mod = 1000000007
#
# triple = map(math.prod, combinations(num, 3))
#
# print(sum(triple) % mod)



# n = int(input())
# num = list(map(int, input().split()))
# mod = 1000000007
#
# ts = 0
# for i in range(n):
#     for j in range(i+1, n):
#         for k in range(j+1, n):
#             ts += (num[i] * num[j] * num[k])
# print(ts % mod)