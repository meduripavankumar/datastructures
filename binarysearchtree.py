class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
            return True
        cur = self.root
        while True:
            if val < cur.val:
                if cur.left is None:
                    cur.left = new_node
                    return True
                cur = cur.left
            elif val > cur.val:
                if cur.right is None:
                    cur.right = new_node
                    return True
                cur = cur.right
            else:
                return False  # Avoid inserting duplicates

    def BFS(self):
        if self.root is None:
            return []  # Return an empty list instead of None
        
        res = []
        queue = [self.root]  # Initialize queue properly
        
        while len(queue) > 0:
            cur = queue.pop(0)
            res.append(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return res
    
    # DFS Inorder (Left -> Root -> Right)
    def dfs_inorder(self):
        res = []
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            res.append(node.val)
            traverse(node.right)
        traverse(self.root)
        return res
    
    # DFS Postorder (Left -> Right -> Root)
    def dfs_postorder(self):
        res = []
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            traverse(node.right)
            res.append(node.val)
        traverse(self.root)
        return res

    # DFS Preorder (Root -> Left -> Right) [Fixed order]
    def dfs_preorder(self):
        res = []
        def traverse(node):
            if not node:
                return
            res.append(node.val)  # Root first
            traverse(node.left)
            traverse(node.right)
        traverse(self.root)
        return res

# Testing the corrected BST implementation
my_bst = BST()

# Insert elements into the BST
my_bst.insert(2)
my_bst.insert(1)
my_bst.insert(3)

# Check root values
print("Root Value:", my_bst.root.val)           # Expected: 2
print("Right Child:", my_bst.root.right.val)    # Expected: 3
print("Left Child:", my_bst.root.left.val)      # Expected: 1

# Perform BFS and DFS Traversals
print("\nBFS Traversal:", my_bst.BFS())         # Expected: [2, 1, 3]
print("DFS Inorder:", my_bst.dfs_inorder())     # Expected: [1, 2, 3] (sorted order)
print("DFS Preorder:", my_bst.dfs_preorder())   # Expected: [2, 1, 3] (Root -> Left -> Right)
print("DFS Postorder:", my_bst.dfs_postorder()) # Expected: [1, 3, 2] (Left -> Right -> Root)
