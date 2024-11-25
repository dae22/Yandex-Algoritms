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


def topsort(tree):
    pass


with open('input.txt', 'r') as f:
    n = int(f.readline().strip())
    data = [f.readline().strip().split() for _ in range(n-1)]

start = time.time()
mid = dict()
for f, s in data:
    if f in mid:
        mid[f].append(s)
    else:
        mid[f] = [s]
del data

sons = []
for el in mid.values():
    sons.extend(el)
for el in mid.keys():
    if el not in sons:
        FATHER = el
        break
del sons

tree = [FATHER]
for el in mid[FATHER]:
    tree.append([el])
del mid[FATHER]
tree_add(tree)
print(f'дерево: {time.time() - start}')