from py_visual_algo.algorithms.trees import preorder_traversal


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


root = Node(1, Node(2, Node(4), Node(5)), Node(3))
print("Preorder Traversal:", list(preorder_traversal(root)))
