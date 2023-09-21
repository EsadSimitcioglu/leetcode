# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    max_depth = 0
    result_node = None
    
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:

        def dfs(node, depth):
            if node is None:
                return depth

            left = dfs(node.left, depth+1)
            right = dfs(node.right, depth+1)

            if left == right:
                self.max_depth = max(left, self.max_depth)

                if self.max_depth == left:
                    self.result_node = node
            
            return max(left,right)

        dfs(root, 0)
        
        return self.result_node


        