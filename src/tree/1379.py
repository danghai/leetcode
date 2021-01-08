# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.dfs(original, cloned, target)
        return self.ans

    def dfs(self, original, cloned, target):
        if not original: return
        if original == target:
            self.ans = cloned
        self.dfs(original.left, cloned.left, target)
        self.dfs(original.right, cloned.right, target)
