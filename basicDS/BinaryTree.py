class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def getDepth(root, depth):
    if root is None:
        return depth

    leftDepth = getDepth(root.left, depth + 1)
    rightDepth = getDepth(root.right, depth + 1)
    return max(leftDepth, rightDepth)


def countFullNodes(root):
    if root is None:
        return 0

    isFull = root.left is not None and root.right is not None

    leftCount = countFullNodes(root.left)
    rightCount = countFullNodes(root.right)

    return isFull + leftCount + rightCount
