"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        indegree = collections.defaultdict(int)
        for node in tree:
            for child in node.children:
                indegree[child.val] += 1
        for node in tree:
            if indegree[node.val] == 0:
                return node
        return None


