from collections import defaultdict
import sys, time

def add_el(tree):
    if tree[0] == a:
        tree.append([b])
        return True
    for i in range(1, len(tree)):
        if add_el(tree[i]):
            return True
    return False


def money(tree, m=0):
    if None in tree:
        del tree[tree.index(None)]
    if len(tree) == 1:
        m += 1
        fnl[tree[0]] += m
    else:
        m += (1 + money(tree[1]))
        fnl[tree[0]] += m
        if len(tree[1]) == 1:
            tree[1] = None
    return m

sys.setrecursionlimit(100000)
with open('input.txt', 'r') as f:
    n = int(f.readline().strip())
    data = list(enumerate(map(int, f.readline().strip().split()), 2))

s = time.time()
tree = [1]
for b, a in data:
    add_el(tree)
print(f'дерево: {time.time() - s}')

s = time.time()
fnl = defaultdict(int)
for i in range(n):
    money(tree)
print(f'бюрократия: {time.time() - s}')

for a, b in sorted(fnl.items()):
    print(b, end=' ')