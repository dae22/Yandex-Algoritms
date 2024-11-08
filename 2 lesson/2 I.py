from collections import Counter

# если 1 - то полезный, если 0 - то интересный

n = int(input())
interes = list(map(int, input().split()))
polza = list(map(int, input().split()))
nastroi = list(map(int, input().split()))

chk_i = sorted(list(zip(interes, polza, range(1, n+1))), key=lambda x: (-x[0], -x[1], x[2]))
chk_p = sorted(list(zip(interes, polza, range(1, n+1))), key=lambda x: (-x[1], -x[0], x[2]))

hashset = dict()
r, l = 0, 0
for el in nastroi:
    if el == 1:
        while True:
            if hash(chk_p[r]) in hashset:
                r += 1
            else:
                break
        print(chk_p[r][2], end=' ')
        hashset[hash(chk_p[r])] = 1
        r += 1
    else:
        while True:
            if hash(chk_i[l]) in hashset:
                l += 1
            else:
                break
        print(chk_i[l][2], end=' ')
        hashset[hash(chk_i[l])] = 1
        l += 1
