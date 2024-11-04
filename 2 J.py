n = int(input())
uliki = list(map(int, input().split()))
m, k = map(int, input().split())
start = list(map(int, input().split()))

prf = [0] * n
l, r, kn = n-1, n-1, 0
while r >= 0:
    while (uliki[l-1] < uliki[l] or (uliki[l-1] == uliki[l] and kn<k)) and l!=0:
        if uliki[l-1] == uliki[l] and kn<k:
            l -= 1
            kn += 1
        else:
            l -= 1
    if l == 0:
        for i in range(l,r+1):
            prf[i] = 1
        break
    prf[r] = l + 1
    if l != 0 and uliki[l-1] > uliki[l]:
        for i in range(l, r+1):
            prf[i] = l+1
        l -= 1
        r = l
        kn = 0
        continue
    if (uliki[l-1] == uliki[l] and kn>=k):
        if uliki[r-1] == uliki[r]:
            kn -= 1
        r -= 1

for el in start:
    print(prf[el-1], end=' ')