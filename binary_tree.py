from node import Node


class BinaryTree:
    root = None

    def __init__(self, node: Node) -> None:
        self.root = node if node else Node("rooooot")

    def inorder_traversal(self, node):
        node = self.root if node is None else node

        if node.left:
            print(node.left.data, end="")
            self.inorder_traversal(node.left)

        if node.right:
            print(node.right.data, end="")
            self.inorder_traversal(node.right)
        else:
            print(end="")
            return

    def postorder_traversal(self, node: Node = None):
        node = self.root if node is None else node
        if node.left:
            self.postorder_traversal(node.left)

        if node.right:
            self.postorder_traversal(node.right)
        print(node.data, end="")

    def height(self, node=None):
        hleft = 0
        hright = 0
        node = self.root if node is None else node
        if not node.left and not node.right:
            return 0
        if node.left:
            hleft = self.height(node=node.left)
        if node.right:
            hright = self.height(node=node.right)
        return max(hleft+1, hright+1)
