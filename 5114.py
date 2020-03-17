'''
$5114. Delete Tree Nodes
'''



class Solution:
    def deleteTreeNodes(self, nodes, parent, value):
        for i in range(nodes-1, -1, -1):
            if parent[i] == -1:
                continue
            value[parent[i]] += value[i]
        for i in range(nodes):
            if parent[i] == -1:
                continue
            if value[parent[i]] == 0:
                value[i] = 0
        for i in range(nodes):
            if value[i] == 0:
                nodes -= 1
        return nodes

sol = Solution()
nodes = 7
parent = [-1,0,0,1,2,2,2]
value = [1,-2,4,0,-2,-1,-1]
print(sol.deleteTreeNodes(nodes, parent, value))