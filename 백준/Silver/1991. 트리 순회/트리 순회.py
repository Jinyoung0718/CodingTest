n = int(input())
tree = {}

for _ in range(n):
    parent, left, right = input().split()
    tree[parent] = [left if left != '.' else None, right if right != '.' else None]


def preOrder(root, result):
    if root is None:
        return 
    
    result.append(root)
    if tree[root][0]:
        preOrder(tree[root][0], result)
    if tree[root][1]:
        preOrder(tree[root][1], result)
    
    return result

def inOrder(root, result):
    if root is None:
        return 
    
    if tree[root][0]:
        inOrder(tree[root][0], result)
        
    result.append(root)

    if tree[root][1]:
        inOrder(tree[root][1], result)
    return result

def postOrder(root, result):
    if root is None:
        return 
    
    if tree[root][0]:
        postOrder(tree[root][0], result)
    if tree[root][1]:
        postOrder(tree[root][1], result)
    
    result.append(root)
    return result

print("".join(preOrder('A', [])))
print("".join(inOrder('A', [])))
print("".join(postOrder('A', [])))