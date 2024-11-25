from collections import defaultdict
import sys

def add_el(tree):
    if tree[0] in mid:
        tree.extend(mid[tree[0]])
        del mid[tree[0]]
    for i in range(1, len(tree)):
        add_el(tree[i])
    return tree


def money(tree, m=0, q=0):
    if len(tree) > 1:
        for i in range(1, len(tree)):
            x, y = money(tree[i])
            m += (x + y)
            q += y
    m += 1
    q += 1
    fnl[tree[0]] = m
    return (m, q)


sys.setrecursionlimit(1000000)
with open('input.txt', 'r') as f:
    n = int(f.readline().strip())
    data = list(enumerate(map(int, f.readline().strip().split()), 2))

mid = defaultdict(list)
for b, a in data:
    mid[a].append([b])
del data

tree = [1]
add_el(tree)

fnl = defaultdict(int)
money(tree)

for a, b in sorted(fnl.items()):
    print(b, end=' ')