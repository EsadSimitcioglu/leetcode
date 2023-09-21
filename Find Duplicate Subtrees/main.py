# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        hmap = {}
        res = []
    
        def serialization(node, path):

            if node is None: return "#"

            path = str(node.val) + "," + serialization(node.left, path) + serialization(node.right, path)

            if path in hmap:
                hmap[path] += 1
                
                if hmap[path] == 2:
                    res.append(node)
            else:
                hmap[path] = 1
            
            return path

        serialization(root, '')
        print(res)
        print(hmap)
        return res
        


