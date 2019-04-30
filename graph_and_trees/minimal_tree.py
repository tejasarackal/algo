from graph_and_trees.TreeNode import TreeNode


def minimal_bst(arr:[], start, end):
    if end < start:
        return None

    mid = int((start + end)/2)
    cur = TreeNode(arr[mid])
    cur.left = minimal_bst(arr, start, mid - 1)
    cur.right = minimal_bst(arr, mid + 1, end)

    return cur


def minimal_tree(arr: []) -> TreeNode:
    return minimal_bst(arr, 0, len(arr) - 1)


if __name__ == '__main__':
    sorted_ls = [1,2,3,4,5]
    root = minimal_tree(sorted_ls)
    print(root.left.right.label, root.left.label, root.label, root.right.label, root.right.right.label)
