# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    if root is None:
        return []
    else:
        traversal = []
        traversal += inorderTraversal(root.left)
        traversal.append(root.val)
        traversal += inorderTraversal(root.right)
        return traversal

# Example usage:
# Constructing a binary tree: [1,2,3]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print(inorderTraversal(root))  # Output: [2, 1, 3]
