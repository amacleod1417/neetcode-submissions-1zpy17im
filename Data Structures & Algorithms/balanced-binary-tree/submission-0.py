# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def height(self, root: Optional[TreeNode]):
        if not root:
            return 0

        right = self.height(root.right)
        left = self.height(root.left)
        return 1 + max(left, right)



    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        right = self.isBalanced(root.right)
        left = self.isBalanced(root.left)

        if abs(self.height(root.right) - self.height(root.left)) < 2 and right == True and left == True:
            return True
        else:
            return False

    

    

        
    

            
