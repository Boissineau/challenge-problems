# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def buildTree(preorder, inorder):
        def array_to_tree(left, right):
            nonlocal preorder_index
            if left > right: return None 
            val = preorder[preorder_index]
            root = TreeNode(val)
            preorder_index += 1 

            root.left = array_to_tree(left, memo[val] - 1)
            root.right = array_to_tree(memo[val] + 1, right)
            return root 

        
        preorder_index = 0 
        memo = {} 
        for idx, val in enumerate(inorder):
            memo[val] = idx 
        return array_to_tree(0, len(preorder) - 1)

        

if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    sol = Solution.buildTree(preorder=preorder, inorder=inorder)

                 
            






        
