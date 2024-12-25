class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


def inorder_traversal(node):
    """Generator for Inorder Traversal."""
    if node:
        yield from inorder_traversal(node.left)
        yield node.value
        yield from inorder_traversal(node.right)


def preorder_traversal(node):
    """Generator for Preorder Traversal."""
    if node:
        yield node.value
        yield from preorder_traversal(node.left)
        yield from preorder_traversal(node.right)


def postorder_traversal(node):
    """Generator for Postorder Traversal."""
    if node:
        yield from postorder_traversal(node.left)
        yield from postorder_traversal(node.right)
        yield node.value
