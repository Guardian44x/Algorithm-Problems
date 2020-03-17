"""
$5296. All Elements in Two Binary Search Trees
"""

class Solution:
    def getAllElements(self, root1, root2):
        
        def TreeFlatten(root):
            res = []
            if root == None:
                return []
            nodes = [root]
            while nodes:
                node = nodes.pop(0)
                if node != None:
                    res.append(node.val)
                    nodes.append(node.left)
                    nodes.append(node.right)
            return res
        
        flatten1 = TreeFlatten(root1)
        flatten2 = TreeFlatten(root2)

        res = flatten1 + flatten2
        res.sort()

        return res