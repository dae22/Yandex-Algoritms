def tree_add(tree):
    for i in range(1, len(tree)):
        if tree[i][0] in mid:
            for el in mid[tree[i][0]]:
                tree[i].append([el])
            del mid[tree[i][0]]
    for i in range(1, len(tree)):
        tree_add(tree[i])
    return tree

def search_tree(tree, d=0):
    fnl.append((tree[0], d))
    for i in range(1,len(tree)):
        search_tree(tree[i], d+1)

with open('input.txt', 'r') as f:
    n = int(f.readline().strip())
    data = [f.readline().strip().split() for _ in range(n-1)]

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
fnl = []
search_tree(tree)
fnl.sort(key=lambda x: x[0])
for el in fnl:
    print(*el)
