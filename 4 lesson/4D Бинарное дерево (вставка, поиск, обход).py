def add_tree(el, tree):
    if el == tree[0]:
        print('ALREADY')
    elif tree[0] is None:
        tree = [el, None, None]
        print('DONE')
    elif el > tree[0]:
        if tree[2] is None:
            tree[2] = [el, None, None]
            print('DONE')
        else:
            add_tree(el, tree[2])
    elif el < tree[0]:
        if tree[1] is None:
            tree[1] = [el, None, None]
            print('DONE')
        else:
            add_tree(el, tree[1])
    return tree

def search_tree(el, tree):
    if tree[0] is None:
        return False
    elif tree[0] == el:
        return True
    elif  not tree[1] is None and el < tree[0]:
        return search_tree(el, tree[1])
    elif not tree[2] is None and el > tree[0]:
        return search_tree(el, tree[2])

def print_tree(tree, deep=0):
    if tree[0] is None:
        return
    if not tree[1] is None:
        print_tree(tree[1], deep+1)
        print('.' * deep, tree[0], sep='')
        if not tree[2] is None:
            print_tree(tree[2], deep+1)
    else:
        print('.' * deep, tree[0], sep='')
        if not tree[2] is None:
            print_tree(tree[2], deep + 1)


Tree = [None]
macros = {'ADD': 'Tree = add_tree(el, Tree)', 'SEARCH': 'print("YES" if search_tree(el, Tree) else "NO")', 'PRINTTREE': 'print_tree(Tree)'}
with open('input.txt', 'r') as f:
    data = f.readlines()
for el in data:
    row = list(el.strip().split())
    if len(row) > 1:
        do, el = row[0], int(row[1])
    else:
        do = row[0]
    exec(macros[do])
