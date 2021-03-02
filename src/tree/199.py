'''
TC : O(n) traversal every node for each level
SC : O(n) save all node in dict_t
'''
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        
        dict_t = collections.defaultdict(list)
        self.dfs(dict_t,root,0)
        A = []
        for val in dict_t.values():
            A.append(val.pop())
        return A
    def dfs(self,dict_t,root,level):
        if not root:
            return None
        dict_t[level].append(root.val)
        self.dfs(dict_t,root.left,level+1)
        self.dfs(dict_t,root.right,level+1)
        
