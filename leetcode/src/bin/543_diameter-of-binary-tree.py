'''
给你一棵二叉树的根节点，返回该树的 直径 。
二叉树的 直径 是指树中任意两个节点之间最长路径的 长度 。这条路径可能经过也可能不经过根节点 root 。
两节点之间路径的 长度 由它们之间边数表示。

示例 1：
输入：root = [1,2,3,4,5]
输出：3
解释：3 ，取路径 [4,2,1,3] 或 [5,2,1,3] 的长度。
示例 2：
输入：root = [1,2]
输出：1
'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def max_depth(root: Optional[TreeNode], ans: TreeNode) -> int:
            if not root:
                return 0
            depth_l = max_depth(root.left, ans)
            depth_r = max_depth(root.right, ans)
            diam = 1 + depth_l + depth_r
            ans.val = max(ans.val, diam)
            return 1 + max(depth_l, depth_r)

        ans = TreeNode(0)
        max_depth(root, ans)
        return ans.val - 1
        

if __name__ == "__main__":
    root = TreeNode(2, TreeNode(1), TreeNode(3, TreeNode(5, TreeNode(7)), TreeNode(4)))
    sol = Solution()
    ans = sol.diameterOfBinaryTree(root)
    print(f"ans:{ans}")

    root = TreeNode(2, TreeNode(1), TreeNode(3, TreeNode(5, TreeNode(7, TreeNode(9))), TreeNode(4, TreeNode(6, TreeNode(8)))))
    sol = Solution()
    ans = sol.diameterOfBinaryTree(root)
    print(f"ans:{ans}")

    '''
    show = ShowTree()
    ans = show.inorder(ans)
    print(f"ans:{ans}")
    '''

