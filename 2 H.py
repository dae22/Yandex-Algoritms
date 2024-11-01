from functools import reduce
from math import prod

n = int(input())
cab = list(map(int, input().split()))
# with open('input.txt', 'r') as f:
#     n = int(f.readline().rstrip())
#     cab = list(map(int, f.readline().rstrip().split()))

print(cab)

# m = 99999999999999999999999
# for i in range(n):
#     s = 0
#     for j in range(n):
#         if i != j:
#             s += abs(i-j)*cab[j]
#             if s > m:
#                 break
#     m = min(m, s)
# print(m)
