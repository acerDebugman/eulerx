'''
给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素(从 1 开始计数).
输入：root = [3,1,4,null,2], k = 1
输出：1
输入：root = [5,3,6,2,4,null,null,1], k = 3
输出：3
'''

from typing import Optional,List
from print_tools import ShowTree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root: Optional[TreeNode], k: TreeNode) -> int:
            if not root:
                return -1
            ans_l = dfs(root.left, k)
            if ans_l != -1:
                return ans_l
            k.val -= 1
            if k.val == 0:
                return root.val
            return dfs(root.right, k)
        return dfs(root, TreeNode(k))

    def kthSmallest2(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1;
        ans_l = self.kthSmallest2(root.left, k)
        if ans_l != -1 and k == 0:
            return ans_l
        if k == 0:
            return root.val
        ans_r = self.kthSmallest2(root.right, k - 1)
        if ans_r != -1 and k-1 == 0:
            return ans_r
        return -1


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(2), TreeNode(5, TreeNode(4), TreeNode(6)))
    show = ShowTree()
    print(show.inorder(root))
    sol = Solution()
    ans = sol.kthSmallest2(root, 3)
    print(f"ans:{ans}")
    

   
