import sys


n, m = map(int, input().split())
weight = list(map(int, input().split()))
costs = list(map(int, input().split()))

if min(weight) > m:
    sys.exit()

options = [0 if i == 0 else -1 for i in range(m + 1)]
arr = [-1 for _ in range(m + 1)]
arr_arr = [[] for _ in range(n + 1)]
for i in range(n):
    for j in range(m - weight[i], -1, -1):
        if options[j] != -1:
            nw = j + weight[i]
            nc = options[j] + costs[i]
            if options[nw] == -1 or options[nw] < nc:
                options[nw] = nc
                arr[nw] = i
    arr_arr[i] = arr.copy()

max_cost = max(options)
index = options.index(max_cost)
item_index = arr[index]
result = []
while True:
    if (item_index + 1) in result:
        item_index -= 1
    if item_index < 0:
        break
    item_index = arr_arr[item_index][index]
    result.append(item_index + 1)
    index -= weight[item_index]
    if index <= 0:
        break

result.sort()
print(*result, sep='\n')
