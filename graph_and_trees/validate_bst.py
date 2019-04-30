from graph_and_trees.TreeNode import TreeNode


def validate_bst(node: TreeNode, parent_min: int, parent_max: int) -> bool:
    if not node:
        return True

    if (parent_min and node.label <= parent_min) or (parent_max and node.label > parent_max):
        return False

    if not validate_bst(node.left, parent_min, node.label) or not validate_bst(node.right, node.label, parent_max):
        return False

    return True


def validate_tree(node: TreeNode):
    return validate_bst(node, None, None)


if __name__ == '__main__':
    root = TreeNode(20)
    root.right = TreeNode(22)
    root.left = TreeNode(18)
    root.left.left = TreeNode(17)
    root.left.right = TreeNode(19)
    root.right.right = TreeNode(24)

    print(validate_tree(root))
