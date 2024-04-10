'''
给你一个二叉树的根节点 root ， 检查它是否轴对称。

示例 1：
输入：root = [1,2,2,3,4,4,3]
输出：true
示例 2：
输入：root = [1,2,2,null,3,null,3]
输出：false
'''

from print_tools import ShowTree
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def _is_sym(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if left == right == None:
                return True
            if not left or not right or left.val != right.val:
                return False

            return _is_sym(left.left, right.right) and _is_sym(left.right, right.left)
        return _is_sym(root.left, root.right)


if __name__ == "__main__":
    root = TreeNode(2, TreeNode(3), TreeNode(3))
    sol = Solution()
    ans = sol.isSymmetric(root)
    print(f"ans:{ans}")
    #show = ShowTree()
    #s = show.inorder(ans)
    #print(f"show:{s}")

    root = TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(5), TreeNode(4)))
    sol = Solution()
    ans = sol.isSymmetric(root)
    print(f"ans:{ans}")
