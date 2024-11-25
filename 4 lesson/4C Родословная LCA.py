import sys
import time


sys.setrecursionlimit(100000)
def tree_add(tree):
    l = len(tree)
    for i in range(1, l):
        if tree[i][0] in mid:
            for el in mid[tree[i][0]]:
                tree[i].append([el])
            del mid[tree[i][0]]
    for i in range(1, l):
        tree_add(tree[i])
    return tree


def LCA(tree, d=0):
    for i in range(1, len(tree)):
        x = LCA(tree[i])
        if x[1]:
            return (0, True)
        d += x[0]
    if tree[0] == a: d += 1
    if tree[0] == b: d += 1
    if d == 2:
        print(tree[0])
        return (0, True)
    return (d, False)


with open('input.txt', 'r') as f:
    n = int(f.readline().strip())
    data = [f.readline().strip().split() for _ in range(n-1)]
    req = [tuple(el.strip().split()) for el in f.readlines()]

start = time.time()
mid = dict()
for s, f in data:
    if f in mid:
        mid[f].append(s)
    else:
        mid[f] = [s]
del data

son = []
for el in mid.values():
    son.extend(el)
for el in mid.keys():
    if el not in son:
        FATHER = el
        break
del son
tree = [FATHER]
for el in mid[FATHER]:
    tree.append([el])
del mid[FATHER]

tree_add(tree)
print(f'дерево: {time.time() - start}')


s = time.time()
memo = dict()
for a, b in req:
    # if (a, b) in memo:
    #     print(memo[(a, b)])
    if a == b:
        print(a)
    else:
        LCA(tree)
f = time.time()
print(f-s)