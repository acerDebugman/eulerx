'''
给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。
'''

'''
这题的思路是用先序遍历的第一个节点找到中序遍历的根节点，这样中序遍历就可以区分左右子树;然后用左右子树的长度可以在先序遍历的数组里划分出来先序遍历的左右子树部分。然后再找先序遍历的左右子树的第一个节点，这样递归的判断.
这题的重点是要使用前序遍历和中序遍历的特点,将每次将原本的前序遍历和中序遍历的左右子树分开。先用前序遍历的第一个节点将中序遍历的左右子树分开，在用左右子树的长度，将前序遍历分开为左右子树，这样再递归的产生节点。当前序遍历或者中序遍历的数组为空的时候，就结束递归。
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
    def buildTree2(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        print(preorder, inorder) 
        if not inorder or not preorder:
            return None

        v = preorder[0]
        v_in = inorder.index(v) 
        # 用这种方式,只能选择找中序遍历的根节点的前一个,这样在前序遍历里找的都是左子树。
        # 不能用中序遍历的根节点的后一个,因为后一个不能在前序遍历里将左右子树分开！
        if v_in-1 >= 0 and inorder[v_in-1] in preorder:
            l_pre = preorder.index(inorder[v_in-1])
        else:
            l_pre = 1

        node = TreeNode(v)
        node.left = self.buildTree2(preorder[1:l_pre+1], inorder[:v_in])
        node.right = self.buildTree2(preorder[l_pre+1:], inorder[v_in+1:])
        return node

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not preorder:
            return None

        v = preorder[0]
        # v_in+1 也可以当做inorder的左子树，右子树的长度
        # 这里可以优化，使用map来保存中序的位置
        v_in = inorder.index(v) 

        node = TreeNode(v)
        # 这里v_in也当做左子树也右子树的长度了！不用index的方式
        node.left = self.buildTree(preorder[1:v_in+1], inorder[:v_in])
        node.right = self.buildTree(preorder[v_in+1:], inorder[v_in+1:])
        return node
    
if __name__ == "__main__":
    root = TreeNode(3, TreeNode(2), TreeNode(5, TreeNode(4), TreeNode(6)))
    show = ShowTree()
    print(show.inorder(root))
    print(show.preorder(root))
    pre_lst = show.preorder(root)
    in_lst = show.inorder(root)

    sol = Solution()
    ans = sol.buildTree2(pre_lst, in_lst)
    print(f"ans:{show.inorder(ans)}")
    

   
