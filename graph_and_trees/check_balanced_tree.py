from .TreeNode import TreeNode


def check_balanced_tree(root: TreeNode) -> tuple():
    if not root:
        return True, -1

    isBalanceLeft, heightLeft = check_balanced_tree(root.left)
    isBalanceRight, heightRight = check_balanced_tree(root.right)

    if not isBalanceRight:
        return False, -1

    if not isBalanceLeft:
        return False, -1

    if abs(heightLeft - heightRight) > 1:
        return False, -1
    else:
        return True, max(heightLeft, heightRight) + 1


if __name__ == '__main__':
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(5)
    root.left.right.right = TreeNode(6)

    print(check_balanced_tree(root))
