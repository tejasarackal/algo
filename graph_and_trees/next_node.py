from graph_and_trees.TreeNode import TreeNodeP


def leftmost_child(node: TreeNodeP) -> TreeNodeP:
    if not node:
        return None

    _left = node
    while _left and _left.left:
        _left = _left.left

    return _left


def next_node(node: TreeNodeP) -> TreeNodeP:
    if not node:
        return None

    if node.right:
        return leftmost_child(node.right)
    else:
        super = node.parent
        sub = node
        while super and super.right == sub:
            sub = super
            super = sub.parent

        return super


if __name__ == '__main__':
    root = TreeNodeP(5)
    root.right = TreeNodeP(7)
    root.left = TreeNodeP(3)
    root.right.right = TreeNodeP(8)
    root.right.left = TreeNodeP(6)
    root.left.left = TreeNodeP(1)
    root.left.right = TreeNodeP(4)

    root.right.parent = root
    root.left.parent = root

    root.right.right.parent = root.right
    root.right.left.parent = root.right

    root.left.right.parent = root.left
    root.left.left.parent = root.left

    _next = next_node(root.right)

    print(_next.label)
