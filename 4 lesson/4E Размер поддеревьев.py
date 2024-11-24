import sys
import time
s = time.time()

def add_el(tree, found=False):
    if found:
        return True
    if tree[0] == a:
        tree.append([b])
        return True
    for subtree in tree[1:]:
        if add_el(subtree, False):
            return True
    return False


def count_tree(tree, d=0):
    for i in range(1, len(tree)):
        d += (1 + count_tree(tree[i]))
    fnl.append((tree[0], d+1))
    return d


def prepair():
    for i in range(len(data)):
        data[i].sort()
    data.sort()
    exist = dict()
    for el in data[0]:
        exist[el] = 0
    mid = [data.pop(0)]
    while True:
        if not len(data):
            break
        r = 0
        while r < len(data):
            if data[r][0] in exist:
                mid.append([data[r][0], data[r][1]])
                for el in data.pop(r):
                    exist[el] = 0
            elif data[r][1] in exist:
                mid.append([data[r][1], data[r][0]])
                for el in data.pop(r):
                    exist[el] = 0
            else:
                r += 1
    return mid

sys.setrecursionlimit(100000)
with open('input.txt', 'r') as f:
    n = int(f.readline().strip())
    data = [list(map(int, f.readline().strip().split())) for _ in range(n-1)]

start = time.time()
mid = prepair()
finish = time.time()
print(f'время подготовки: {finish - start}')

start = time.time()
tree = [1]
for a, b in mid:
    flag = False
    add_el(tree)
finish = time.time()
print(f'время дерева: {finish - start}')

start = time.time()
fnl = []
count_tree(tree)
fnl.sort(key=lambda x: x[0])
finish = time.time()
print(f'время поиска: {finish - start}')

with open('output.txt', 'w') as f:
    for a, b in fnl:
        f.write(f'{b} ')
f = time.time()
print(f'\nвремя проги: {f - s}')