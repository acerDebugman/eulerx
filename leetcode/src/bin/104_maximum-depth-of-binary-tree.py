# binary tree
'''
给定一个二叉树 root ，返回其最大深度。
二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。
示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：3
示例 2：
输入：root = [1,null,2]
输出：2
'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)));
    sol = Solution()
    ans = sol.maxDepth(root)
    print(f"ans: {ans}")

    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7, TreeNode(7))));
    sol = Solution()
    ans = sol.maxDepth(root)
    print(f"ans: {ans}")

    root = TreeNode(3);
    sol = Solution()
    ans = sol.maxDepth(root)
    print(f"ans: {ans}")


