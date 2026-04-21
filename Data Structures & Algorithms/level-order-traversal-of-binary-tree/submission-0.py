# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Handle empty tree
        if not root:
            return []
        
        # Initialize an empty result list
        result = []
        
        # Star of this show is the queue: initialize a queue with the root
        q = deque([root])
        
        # While the queue is not empty
        while q:
            level_size = len(q)
            current_level = []
        
            for _ in range(level_size):
                node = q.popleft()
                current_level.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            result.append(current_level)
        
        return result