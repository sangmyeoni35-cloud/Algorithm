def make_tree(n):
    tree = {}
    for _ in range(n):
        value = input().split()[:3]
        if value[1] == '.':
            value[1] = None
        if value[2] == '.':
            value[2] = None
        tree[value[0]] = [value[1],value[2]]
        # print(tree)
    return tree

def preorder(data):
    if data == None: return
    print(data, end=" ")
    preorder(tree[data][0])
    preorder(tree[data][1])

def inorder(data):
    if data == None: return
    inorder(tree[data][0])
    print(data, end=" ")
    inorder(tree[data][1])

def postorder(data):
    if data == None: return
    postorder(tree[data][0])
    postorder(tree[data][1])
    print(data, end=" ")

n = int(input())
tree = make_tree(n)
# print(tree)
preorder('A')
inorder('A')
postorder('A')
