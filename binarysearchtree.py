class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self,val):
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
            return True
        cur = self.root
        while True:
            if new_node.val < cur.val:
                if cur.left is None:
                    cur.left = new_node
                    return True
                cur = cur.left
            elif new_node.val > cur.val:
                if cur.right is None:
                    cur.right = new_node
                    return True
                cur = cur.right
            else:
                return False
            
    def BFS(self):
        res,queue = []
        if self.root is None:
            return None
        cur = self.root
        queue.append(cur)
        while len(queue) > 0:
            cur = queue.pop(0)
            res.append(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return res
    

# i left the root right
# po root the left right

    def dfs_inorder(self):
        res = []
        def traverse(node):
            if node.left:
                traverse(node.left)
            res.append(node.val)
            if node.right:
                traverse(node.right)
        traverse(self.root)
        return res
    
    def dfs_postorder(self):
        res = []
        def traverse(node):
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
            res.append(node.val)
        traverse(self.root)
        return res

    def dfs_preorder(self):
        res = []
        def traverse(node):
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
            res.append(node.val)
        traverse(self.root)
        return res

my_bst = BST()

my_bst.insert(2)
my_bst.insert(1)
my_bst.insert(3)
print(my_bst.root.val)
print(my_bst.root.right.val)
print(my_bst.root.left.val)
# print(my_bst.root.right.right.val)

