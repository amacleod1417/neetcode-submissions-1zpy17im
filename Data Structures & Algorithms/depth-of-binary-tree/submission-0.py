# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# max_depth = 0

class Solution:
    def __init__(self):
        self.max_depth = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        self.inOrder(root, 1)
        return self.max_depth

    def inOrder(self, root: Optional[TreeNode], depth):
        if root is None:
            return 
        self.inOrder(root.left, depth + 1)
        print(root.val)
        self.inOrder(root.right, depth + 1)

        if depth > self.max_depth:
            self.max_depth = depth
    





        