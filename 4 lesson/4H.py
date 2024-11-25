from collections import defaultdict
from itertools import combinations


def get_unique_vertices(edges):
    vertices = set()
    for edge in edges:
        vertices.update(edge)
    return sorted(vertices)


def generate_all_subsets(vertices):
    subsets = []
    num_vertices = len(vertices)
    for r in range(1, num_vertices + 1):
        for subset in combinations(vertices, r):
            subsets.append(subset)
    return subsets


def chk_subset(subset):
    was = []
    for el in subset:
        for x in cover[el]:
            was.append(x)
    if set(was) == data:
        good.append(subset)


with open('input.txt', 'r') as f:
    n = int(f.readline().strip())
    data = set([tuple(map(int, f.readline().strip().split())) for _ in range(n-1)])
    q = dict(zip(range(1,n+1), map(int, f.readline().strip().split())))

cover = defaultdict(list)
for a, b in data:
    cover[a].append((a,b))
    cover[b].append((a,b))

vertices = set(get_unique_vertices(data))

subsets = generate_all_subsets(vertices)
good = []
for el in subsets:
    chk_subset(el)

fnl = dict()
for el in good:
    cost = 0
    for x in el:
        cost += q[x]
    fnl[cost] = el

m = min(fnl)
combo = fnl[m]
ln = len(combo)
print(m, ln)
print(*combo)