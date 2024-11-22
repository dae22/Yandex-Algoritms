import sys

sys.setrecursionlimit(100000)


def tree_add(tree):
    for i in range(1, len(tree)):
        if tree[i][0] in mid:
            for el in mid[tree[i][0]]:
                tree[i].append([el])
            del mid[tree[i][0]]
    for i in range(1, len(tree)):
        tree_add(tree[i])
    return tree


with open('input.txt', 'r') as f:
    n = int(f.readline().strip())
    data = [f.readline().strip().split() for _ in range(n-1)]
    req = [el.strip().split() for el in f.readlines()]

mid = dict()
for s, f in data:
    if f in mid:
        mid[f].append(s)
    else:
        mid[f] = [s]
data.clear()

son = []
for el in mid.values():
    son.extend(el)
for el in mid.keys():
    if el not in son:
        FATHER = el
        break
son.clear()

tree = [FATHER]
for el in mid[FATHER]:
    tree.append([el])
del mid[FATHER]

tree_add(tree)
print(tree)