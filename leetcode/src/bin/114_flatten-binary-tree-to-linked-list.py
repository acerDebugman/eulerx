'''
给你二叉树的根结点 root ，请你将它展开为一个单链表：
展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null .
展开后的单链表应该与二叉树 先序遍历 顺序相同。
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
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        h = root
        while h:
            if h.left:
                l, r = h.left, h.right
                h.left = None
                h.right = l
                last_r = l
                while last_r and last_r.right:
                    last_r = last_r.right
                last_r.right = r
            h = h.right
                

if __name__ == "__main__":
    root = TreeNode(3, TreeNode(2), TreeNode(5, TreeNode(4), TreeNode(6)))
    show = ShowTree()
    print(show.preorder(root))
    sol = Solution()
    sol.flatten(root)
    print("ans:",show.preorder(root))
    #print(f"ans:{root}")
    

   
