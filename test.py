# Python3 program to find LCA of n1 and
# n2 using one DFS on the Tree

# Maximum number of nodes is 100000 and
# nodes are numbered from 1 to 100000
MAXN = 100001

tree = [0] * MAXN
for i in range(MAXN):
    tree[i] = []

# Storing root to node path
path = [0] * 3
for i in range(3):
    path[i] = [0] * MAXN

flag = False


# Storing the path from root to node
def dfs(cur: int, prev: int, pathNumber: int,
        ptr: int, node: int) -> None:
    global tree, path, flag

    for i in range(len(tree[cur])):
        if (tree[cur][i] != prev and not flag):

            # Pushing current node into the path
            path[pathNumber][ptr] = tree[cur][i]

            if (tree[cur][i] == node):
                # Node found
                flag = True

                # Terminating the path
                path[pathNumber][ptr + 1] = -1
                return

            dfs(tree[cur][i], cur, pathNumber,
                ptr + 1, node)


# This Function compares the path from root
# to 'a' & root to 'b' and returns LCA of
# a and b. Time Complexity : O(n)
def LCA(a: int, b: int) -> int:
    global flag

    # Trivial case
    if (a == b):
        return a

    # Setting root to be first element
    # in path
    path[1][0] = path[2][0] = 1

    # Calculating path from root to a
    flag = False
    dfs(1, 0, 1, 1, a)

    # Calculating path from root to b
    flag = False
    dfs(1, 0, 2, 1, b)

    # Runs till path 1 & path 2 matches
    i = 0
    while (path[1][i] == path[2][i]):
        i += 1

    # Returns the last matching
    # node in the paths
    return path[1][i - 1]


def addEdge(a: int, b: int) -> None:
    tree[a].append(b)
    tree[b].append(a)


# Driver code
if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        n = int(f.readline().strip())
        data = [f.readline().strip().split() for _ in range(n - 1)]
        req = [tuple(el.strip().split()) for el in f.readlines()]

        # Number of nodes
    for el in data:
        addEdge(el[0], el[1])
    for el in req:
        print(LCA(el[0], el[1]))