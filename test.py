def print_tree(tree, deep=0):
    if tree[1] != None:
        print_tree(tree[1], deep+1)
        print('.' * deep, tree[0])
        if tree[2] != None:
            print_tree(tree[2], deep+1)
    else:
        print('.' * deep, tree[0])
        if tree[2] != None:
            print_tree(tree[2], deep + 1)

tree = [7,[3,[1,None, None],[5,None,None]],[10,[8,None,None],[11,None,None]]]
print_tree(tree)