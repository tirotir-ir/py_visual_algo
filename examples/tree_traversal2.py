from py_visual_algo.algorithms.trees import (
    Node,
    inorder_traversal,
    preorder_traversal,
    postorder_traversal,
)


# Build a simple binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


def run_traversals(tree_root):
    """Run tree traversal examples."""
    print("Inorder Traversal:")
    for value in inorder_traversal(tree_root):
        print(value, end=" ")

    print("\nPreorder Traversal:")
    for value in preorder_traversal(tree_root):
        print(value, end=" ")

    print("\nPostorder Traversal:")
    for value in postorder_traversal(tree_root):
        print(value, end=" ")


if __name__ == "__main__":
    print("Tree Traversal Example:")
    run_traversals(root)
