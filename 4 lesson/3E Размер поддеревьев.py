import sys


def add_el(tree, a, b):
    if tree[0] == a:
        tree.append([b])
    else:


def count_tree(tree, d=0):
    for i in range(1, len(tree)):
        d += (1 + count_tree(tree[i]))
    fnl.append((tree[0], d+1))
    return d

        sys.setrecursionlimit(100000)
with open('input.txt', 'r') as f:
    n = int(f.readline().strip())
    data = [list(map(int, f.readline().strip().split())) for _ in range(n-1)]
    data.sort(key=lambda x: x[0])

fnl = []

tree = []

