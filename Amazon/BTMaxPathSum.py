# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxPathSum(self, root: TreeNode) -> int:
    
    max_path = float('-inf')
    
    def gain(node): 
        nonlocal max_path 
        if node is None: return 0
        
        left = max(gain(node.left), 0)
        right = max(gain(node.right), 0)
        
        cur = node.val + left + right 
        max_path = max(cur, max_path)
        

        return node.val + max(left, right)
    
    gain(root)
    return max_path