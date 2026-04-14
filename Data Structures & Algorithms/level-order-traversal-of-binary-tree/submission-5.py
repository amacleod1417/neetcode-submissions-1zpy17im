# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        visited = [root]
        queue = collections.deque()
        queue.append(root)

        while queue:
            length = len(queue)
            level = []
            
            for i in range(length):
                current_node = queue.popleft()
                print(current_node)
                if current_node:
                    level.append(current_node.val)
                    queue.append(current_node.left)
                    queue.append(current_node.right)
            if level:
                print(level)
                res.append(level)
        return res





        
