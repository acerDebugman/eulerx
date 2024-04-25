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
        pass

if __name__ == "__main__":
    root = TreeNode(2, TreeNode(4), TreeNode(3))
    show = ShowTree()
    print(show.inorder(root))
    sol = Solution()
    ans = sol.kthSmallest(root)
    print(f"ans:{ans}")
    

   
