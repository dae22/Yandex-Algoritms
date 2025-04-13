m = int(input())
a = list(map(int, input().split()))


def add_to_full(minutes, cost, i):
    cnt = (m - minutes) // costs[i][0]
    if (m - minutes) % costs[i][0]:
        cnt += 1
    minutes += costs[i][0] * cnt
    cost += costs[i][1] * cnt
    return [minutes, cost]


unit_cost = []
for i in range(len(a)):
    unit_cost.append(2**i)
costs = sorted(zip(a, unit_cost), key=lambda x: x[1]/x[0])

cost = 0
minutes = 0
minimal = 10 ** 9
for i in range(len(a)):
    if i == 0:
        minutes, cost = add_to_full(minutes, cost, i)
    else:
        minutes -= costs[i-1][0]
        cost -= costs[i-1][1]
        minutes, cost = add_to_full(minutes, cost, i)
    minimal = min(cost, minimal)
print(int(minimal))