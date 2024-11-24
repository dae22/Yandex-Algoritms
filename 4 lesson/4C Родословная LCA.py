import sys

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
        if x > 1:
            d += 5
            break
        d += x
    if tree[0] in req:
        d += 1
    if d == 2:
        print(tree[0])
    return d



    # if tree[0] in req:
    #     d += 1
    # if d
    # for el in tree[1:]:
    #     x = LCA(el, req)
    #     if x >= 2:
    #         break
    #     d += x
    # if d == 2:
    #     print(tree[0])
    #     d *= 2
    # return d


with open('input.txt', 'r') as f:
    n = int(f.readline().strip())
    data = [f.readline().strip().split() for _ in range(n-1)]
    req = [tuple(el.strip().split()) for el in f.readlines()]

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
for req in req:
    flag = False
    if req[0] == req[1]:
        print(req[0])
    else:
        LCA(tree)
