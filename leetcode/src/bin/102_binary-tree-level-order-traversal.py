'''
给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。

示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：[[3],[9,20],[15,7]]
示例 2：
输入：root = [1]
输出：[[1]]
示例 3：
输入：root = []
输出：[]
'''

from print_tools import ShowTree
from typing import Optional,List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def _level_order(root: Optional[TreeNode], ans: List[List[int]]) -> Optional[List[List[int]]]:
            que = deque([root])
            ans.append([root.val])
            tmp = []
            while sk:
                tmp.clear()
                while sk:
                    a = sk.pop() 
                    if a:
                        tmp.append(a.left)
                        tmp.append(a.right)
                res = [node.val for node in tmp if node]
                if res:
                    ans.append(res)
                sk.extend(tmp)
        if not root:
            return []
        ans = [] 
        _level_order(root, ans)
        return ans

if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20))
    sol = Solution()
    ans = sol.levelOrder(root)
    print(ans)

    root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, None, TreeNode(5)))
    sol = Solution()
    ans = sol.levelOrder(root)
    print(ans)

    '''
    show = ShowTree()
    ans = show.inorder(ans)
    print(f"ans:{ans}")
    '''

