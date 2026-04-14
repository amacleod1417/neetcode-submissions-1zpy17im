# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  

    def preOrder(self, root: Optional[TreeNode], order: List):

        if not root:
            order.append("#")
            return

        order.append(root.val)
        self.preOrder(root.left, order)
        self.preOrder(root.right, order)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        tree = []
        subtree = []
        
        self.preOrder(root, tree)
        self.preOrder(subRoot, subtree)

        print(tree)
        print(subtree)

        return any(tree[i : i + len(subtree)] == subtree for i in range(len(tree) - len(subtree) + 1))


        

