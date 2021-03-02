class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        '''
        pre-order : root-left-right
        inorder : left - root -right
        TC : O(n)
        SC : O(n)
        '''
        dict_t = collections.defaultdict(list)
        for i, item in enumerate(inorder):
            dict_t[item] = i
        return self.helper(dict_t,0,len(inorder)-1,preorder)
    def helper(self,dict_t,low,high,preorder):
        if low > high:
            return None
        node = preorder.pop(0)
        idx = dict_t[node]
        root = TreeNode(node)
        root.left = self.helper(dict_t,low,idx-1,preorder) # O(log(n)
        root.right = self.helper(dict_t,idx+1,high,preorder)
        return root
