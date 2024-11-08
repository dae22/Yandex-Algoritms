n = int(input())
city = enumerate(map(int, input().split()))

stek = []
answ = [0] * n
for el in city:
    if len(stek) == 0:
        stek.append(el)
    else:
        while len(stek) != 0 and el[1] < stek[-1][1]:
            nw = stek.pop(-1)
            answ[nw[0]] = el[0]
        stek.append(el)
for i in range(n):
    if answ[i] == 0:
        print(-1, end=' ')
    else:
        print(answ[i], end=' ')
