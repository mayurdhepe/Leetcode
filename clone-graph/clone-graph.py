"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        
        nodeMap = {}
        self.dfs(node, nodeMap)
        return nodeMap[node]
    
    
    def dfs(self, node, nodeMap):
        if node in nodeMap:
            return nodeMap[node]    # return the already existing deep copy node
        
        nodeMap[node] = Node(node.val)
        
        for nbr in node.neighbors:
            if nbr in nodeMap:
                 # if child already exists, append to current node neighbors
                nodeMap[node].neighbors.append(nodeMap[nbr])
            else:
                 # create the child as it does not exist
                newNbr = self.dfs(nbr, nodeMap)
                nodeMap[node].neighbors.append(newNbr)
                
        return nodeMap[node]
                
        