# binary-tree
'''
给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。

示例 1：
输入：root = [1,null,2,3]
输出：[1,3,2]
示例 2：
输入：root = []
输出：[]
示例 3：
输入：root = [1]
输出：[1]
'''

from print_tools import print_lst
from typing import Optional,List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def inorder(root: Optional[TreeNode], ans: List[int]):
            if not root:
                return
            if root.left:
                inorder(root.left, ans)
            ans.append(root.val)
            if root.right:
                inorder(root.right, ans)

        inorder(root, ans)
        return ans


if __name__ == "__main__":
    root = TreeNode(1, None, TreeNode(2, TreeNode(3, None, None) ,None))
    sol = Solution()
    ans = sol.inorderTraversal(root)
    print(f"ans:{ans}")
     
    sol = Solution()
    ans = sol.inorderTraversal(None)
    print(f"ans:{ans}")

    root = TreeNode(1)
    sol = Solution()
    ans = sol.inorderTraversal(root)
    print(f"ans:{ans}")

