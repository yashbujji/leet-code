class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter=0
        self.height(root,self.diameter)
        return self.diameter
    
    def height(self,root,diameter):
        if root is None:
            return 0
        lh=self.height(root.left,self.diameter)
        rh=self.height(root.right,self.diameter)
        self.diameter=max(self.diameter,lh+rh)
        return 1+max(lh,rh)