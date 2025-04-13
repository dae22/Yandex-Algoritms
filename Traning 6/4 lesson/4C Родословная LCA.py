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


def elder_search(tree, stack=[]):
    stack.append(tree[0])
    all_eld[tree[0]] = stack.copy()
    if len(tree) > 1:
        for i in range(1, len(tree)):
            elder_search(tree[i], stack)
    stack.pop()
    return

def LCA(a, b):
    eld_a = list(reversed(all_eld[a]))
    eld_b = list(reversed(all_eld[b]))
    for i in range(len(eld_a)):
        if eld_a[i] in eld_b:
            print(eld_a[i])
            break


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

s = time.time()
all_eld = dict()
elder_search(tree)

for a, b in req:
    if a == b:
        print(a)
    else:
        LCA(a, b)