class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def print_preorder(node):
    if node:
        print(node.val, end=" ")
        print_preorder(node.left)
        print_preorder(node.right)


def print_inorder(node):
    if node:
        print_inorder(node.left)
        print(node.val, end=" ")
        print_inorder(node.right)


def print_postorder(node):
    if node:
        print_postorder(node.left)
        print_postorder(node.right)
        print(node.val, end=" ")


if __name__ == "__main__":
    # Constructing the binary tree for "Sanny Hamulong"
    # Root
    root = Node('S')

    # Level 1
    root.left = Node('A')
    root.right = Node('N')

    # Level 2
    root.left.left = Node('N')
    root.left.right = Node('Y')
    root.right.left = Node('H')
    root.right.right = Node('A')

    # Level 3
    root.left.left.left = Node('M')
    root.left.left.right = Node('U')
    root.left.right.left = Node('L')
    root.left.right.right = Node('O')
    root.right.left.left = Node('N')
    root.right.left.right = Node('G')

    print("=== Assessment 3.5 & 3.6: DFS Methods in Tree ===")
    print("Name: Sanny Hamulong")
    print("-" * 50)

    print("PreOrder Traversal  (Root -> Left -> Right):")
    print_preorder(root)
    print("\n")

    print("InOrder Traversal   (Left -> Root -> Right):")
    print_inorder(root)
    print("\n")

    print("PostOrder Traversal (Left -> Right -> Root):")
    print_postorder(root)
    print()