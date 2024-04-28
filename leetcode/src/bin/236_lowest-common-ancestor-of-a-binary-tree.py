'''
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
示例 1：
输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出：3
解释：节点 5 和节点 1 的最近公共祖先是节点 3 。
示例 2：
输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出：5
解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。
示例 3：
输入：root = [1,2], p = 1, q = 2
输出：1
'''

from typing import Optional,List
from print_tools import ShowTree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
思路一：暴力解法，写一个函数，递归判断节点是否在子树下；如果在，就返回true； 这样前序遍历二叉树即可
思路二：递归下降先判断值是否相等，相等返回节点值。在递归返回的时候 判断p,q是否都在左子树，或者是否都在右子树，或者是否分开在左右子树. 如果是分开在左右子树，就可以判断当前的节点是否是最近的公共祖先,就返回当前root节点
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 这里是合并了情况
        if not root or root.val == p.val or root.val == q.val:
            return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if not l and not r:
            return None
        # 这里相当于将最近的公共直接冒泡似的递归返回了
        if l and not r: return l
        if not l and r: return r
        return root

    
if __name__ == "__main__":
    root = TreeNode(3, TreeNode(2), TreeNode(5, TreeNode(4), TreeNode(6)))
    show = ShowTree()
    print(show.inorder(root))
    p = TreeNode(5)
    q = TreeNode(6)
    sol = Solution()
    ans = sol.lowestCommonAncestor(root, p, q)
    print(f"ans:{ans.val}")
    

   
