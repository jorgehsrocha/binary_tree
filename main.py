from binary_tree import BinaryTree
from node import Node

if __name__ == "__main__":
    root = Node(data="*")

    n1 = Node(data="1")
    n2 = Node(data="2")
    n3 = Node(data="3")
    n4 = Node(data="4")
    n5 = Node(data="5*")
    n6 = Node(data="6")
    n7 = Node(data="7")
    n8 = Node(data="8*")
    n9 = Node(data="9*")

    n1.left = n2
    n2.left = n3
    n3.left = n4
    n3.right = n5
    n5.left = n9

    n6.right = n7
    n6.left = n8

    root.left = n1
    root.right = n6

    tree = BinaryTree(node=root)
    tree.inorder_traversal(None)
    print('\n')
    tree.postorder_traversal(None)
    print(f'Height {tree.height()}')
