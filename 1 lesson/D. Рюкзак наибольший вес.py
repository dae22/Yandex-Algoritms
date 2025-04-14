import sys


n, m = map(int, input().split())
slitki = list(map(int, input().split()))

if sum(slitki) <= m:
    print(sum(slitki))
    sys.exit()

options = [False] * (m + 1)
options[0] = True
for el in slitki:
    for i in range(m - el, -1, -1):
        if options[i]:
            options[i + el] = True
        if options[m]:
            print(m)
            sys.exit()

for i in range(m, -1, -1):
    if options[i]:
        print(i)
        break


# 10 400
# 23 34 29 594 450 14 382 043 10 7362