from py_visual_algo.algorithms.trees import Node, inorder_traversal

# Create a simple binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Perform inorder traversal
print("Inorder Traversal:")
for value in inorder_traversal(root):
    print(value, end=" ")
