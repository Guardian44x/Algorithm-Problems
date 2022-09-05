"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        nqueue = [root]
        res = []
        while len(nqueue) > 0:
            news = []
            vals = []
            # print(nqueue)
            for cur in nqueue:
                vals.append(cur.val)
                if cur.children is not None:
                    news.extend(cur.children)
            nqueue = news
            res.append(vals)
        return res
        