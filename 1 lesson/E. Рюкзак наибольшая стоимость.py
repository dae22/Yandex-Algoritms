import sys


n, m = map(int, input().split())
weight = list(map(int, input().split()))
costs = list(map(int, input().split()))

if sum(weight) <= m:
    print(sum(costs))
    sys.exit()

options = [-1] * (m + 1)
options[0] = 0
for i in range(n):
    for j in range(m - weight[i], -1, -1):
        if options[j] > -1:
            nw = j + weight[i]
            nc = options[j] + costs[i]
            if options[nw] == -1:
                options[nw] = nc
            else:
                options[nw] = max(nc, options[nw])

print(max(options))