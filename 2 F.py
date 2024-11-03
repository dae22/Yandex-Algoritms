n = int(input())
num = list(map(int, input().split()))
s = 0
pref = [0]*(n-2)

for i in range(0, n-2):
    pref[i] = num[i+1] * sum(num[i+2:])

for i in range(n):
    s += num[i] * sum(pref[i:])

print(s % 1000000007)

print(pref)


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
