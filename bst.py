class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.leftChild = left
        self.rightChild = right


node1 = TreeNode(25)
node2 = TreeNode(75)
root = TreeNode(50, node1, node2)


def search(value, node):
    if node is None or node.value == value:
        return node

    elif value < node.value:
        return search(value, node.leftChild)

    else:
        return search(value, node.rightChild)


def insertion(value, node):
    if value < node.value:
        if node.leftChild is None:
            node.leftChild = TreeNode(value)
        else:
            insertion(value, node.leftChild)

    elif value > node.value:
        if node.rightChild is None:
            node.rightChild = TreeNode(value)
        else:
            insertion(value, node.rightChild)


def lift(node, nodetodel):
    if node.leftChild:
        node.leftChild = lift(node.leftChild, nodetodel)

        return node

    else:
        nodetodel.value = node.value

        return node.rightChild

def delete(value, node):
    if node is None:
        return None

    elif value < node.value:
        node.leftChild = delete(value, node.leftChild)

        return node

    elif value > node.value:
        node.rightChild = delete(value, node.rightChild)

        return node

    elif value == node.value:
        if node.leftChild is None:
            return node.rightChild

        elif node.rightChild is None:
            return node.leftChild

        else:
            node.rightChild = lift(node.rightChild, node)

            return node






insertion(100, root)
insertion(67, root)
insertion(82, root)
insertion(46, root)
insertion(115, root)
insertion(53, root)
insertion(1, root)
insertion(70, root)
insertion(12, root)



def traverse_and_print(node):
    if node is None:
        return
    traverse_and_print(node.leftChild)
    print(node.value, end='  ')
    traverse_and_print(node.rightChild)



def max(node):
    if node.rightChild:
        return max(node.rightChild)
    else:
        return node.value


m = {}

def topView(root, dist=0, level=0):
    if root is None:
        return



    topView(root.leftChild, dist - 1, level + 1)
    if dist not in m or m[dist][1] > level:
        m[dist] = [root, level]
    topView(root.rightChild, dist + 1, level + 1)


    return m.values()



traverse_and_print(root)

print(max(root))

y = topView(root)

for value in y:
    print(value[0].value, end=' ')