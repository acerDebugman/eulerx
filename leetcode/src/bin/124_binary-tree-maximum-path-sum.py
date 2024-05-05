'''
二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。
路径和 是路径中各节点值的总和。
给你一个二叉树的根节点 root ，返回其 最大路径和 。

示例 1：
输入：root = [1,2,3]
输出：6
解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
示例 2：
输入：root = [-10,9,20,null,null,15,7]
输出：42
解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42
'''

'''
题解：这个其实需要先理解清楚题意就可以。路径是指一个节点的出度和入度都是1或者0(终端节点)的才是节点序列，才是路径。所以每次递归，要么走左边，要么走右边，就看那边的收益大！收益的计算就是 当前节点val+max(左分支最大，右分支最大), 而路径的最大就是左边最大，和右边最大 加上当前节点值,再和历史最大值比较即可！
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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def maxdfs(root: Optional[TreeNode], ans:TreeNode) -> int:
            if not root:
                return 0
            lmax = max(maxdfs(root.left, ans), 0)
            rmax = max(maxdfs(root.right, ans), 0)
            cur_v = root.val + lmax + rmax
            #print(root.val, lmax, rmax)
            ans.val = max(ans.val, cur_v)
            # 返回的是要么左节点，要么右节点
            return root.val + max(lmax, rmax)

        ans = TreeNode(float("-inf"))
        maxdfs(root, ans)
        return ans.val


if __name__ == "__main__":
    show = ShowTree()
    #root = TreeNode(3, TreeNode(2), TreeNode(5, TreeNode(4), TreeNode(6)))
    #lst = [-10,9,20,None,None,15,7]
    #lst = [-3]
    lst = [-1,-2]
    #print("origin:", lst)
    root = show.build_tree_from_level_order_lst(lst)
    print(show.inorder(root))
    print(show.levelorder(root))
    sol = Solution()
    ans = sol.maxPathSum(root)
    print(f"ans:{ans}")
    

   
