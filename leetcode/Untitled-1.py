# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def reverseOddLevels(self, root):
        q = [root]
        level = 0
        while q[0]:
            if level%2==1:
                for i in range(len(q)//2):
                    left, right = i, len(q)-1-i
                    x, y = q[left], q[right]
                    x.val, y.val = y.val, x.val
            q2 = list()
            for node in q:
                q2.extend([node.left, node.right])
            q = q2
            level += 1
            print("level, q: ", level, q)
        return root

root = TreeNode(1)
left = TreeNode(2)
right = TreeNode(3)
root.left = left 
root.right = right 
so = Solution()
so.reverseOddLevels(root)
print(root.val, root.left.val, root.right.val)