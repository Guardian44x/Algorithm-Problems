"""
$919. Complete Binary Tree Inserter
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.get_leaves()
        
    def get_leaves(self):
        if not self.root:
            return []
        nodes = [self.root]
        self.leaves = []
        while len(nodes) > 0:
            next_nodes = []
            for node in nodes:
                if node.left != None:
                    next_nodes.append(node.left)
                if node.right != None:
                    next_nodes.append(node.right)
                else:
                    self.leaves.append(node)
            nodes = next_nodes

    def insert(self, v: int) -> int:
        insert_node = TreeNode(v)
        leaf = self.leaves[0]
        
        if leaf.left == None:
            leaf.left = insert_node
            self.leaves.append(insert_node)
        else:
            leaf.right = insert_node
            self.leaves.append(insert_node)
            self.leaves.pop(0) 
        return leaf.val
    
    def get_root(self) -> TreeNode:
        return self.root