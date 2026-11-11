from collections import deque


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


class BinaryTreeTraversal:
    def __init__(self):
        self.root = None

    # ==========================================
    # BREADTH-FIRST SEARCH (BFS) FUNCTION
    # ==========================================
    def breadth_first_search(self, root):
        if not root:
            return

        queue = deque([root])
        result = []

        while queue:
            curr = queue.popleft()
            result.append(curr.data)

            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        print("Binary Tree BFS Traversal:", " -> ".join(result))

    # ==========================================
    # DEPTH-FIRST SEARCH (DFS) FUNCTION
    # ==========================================
    def depth_first_search(self, root):
        if not root:
            return

        stack = [root]
        result = []

        while stack:
            curr = stack.pop()
            result.append(curr.data)

            # Push right first so left is processed first in pre-order DFS
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)

        print("Binary Tree DFS Traversal:", " -> ".join(result))


if __name__ == "__main__":
    # Constructing Binary Tree using HAMULONG structure
    tree = BinaryTreeTraversal()
    tree.root = Node('H')
    tree.root.left = Node('A')
    tree.root.right = Node('M')
    tree.root.left.left = Node('U')
    tree.root.left.right = Node('L')
    tree.root.right.left = Node('O')
    tree.root.right.right = Node('N')
    tree.root.left.left.left = Node('G')

    # Calling BFS and DFS separately
    print("--- Running Binary Tree Traversals ---")
    tree.breadth_first_search(tree.root)
    tree.depth_first_search(tree.root)