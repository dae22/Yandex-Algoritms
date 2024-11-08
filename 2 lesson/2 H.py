n = int(input())
cab = list(map(int, input().split()))

pref = [0] * n
p = cab[0]
for i in range(1, n):
    pref[i] = pref[i-1] + p
    p += cab[i]

pref1 = [0] * n
p = cab[-1]
for i in range (-2, -n-1, -1):
    pref1[i] = pref1[i+1] + p
    p += cab[i]

fnl = list(map(lambda x, y: x+y, pref, pref1 ))
print(min(fnl))







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


