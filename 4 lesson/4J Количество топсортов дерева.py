import sys


def add_el(tree):
    if tree[0] == a:
        tree.append([b])
        return True
    for i in range(1, len(tree)):
        if add_el(tree[i]):
            return True
    return False

sys.setrecursionlimit(100000)
with open('input.txt', 'r') as f:
    n = int(f.readline().strip())
    data = [list(map(int, f.readline().strip().split())) for _ in range(n-1)]

x, y = data.pop(0)
tree = [x, [y]]
for a, b in data:
    add_el(tree)

print(tree)
