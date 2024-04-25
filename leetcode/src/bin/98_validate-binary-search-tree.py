'''
给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。有效 二叉搜索树定义如下：
节点的左子树只包含 小于 当前节点的数。
节点的右子树只包含 大于 当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。

示例 1：
输入：root = [2,1,3]
输出：true
示例 2：
输入：root = [5,1,4,null,null,3,6]
输出：false
解释：根节点的值是 5 ，但是右子节点的值是 4 
'''


from typing import List,Optional
from print_tools import ShowTree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid_bst(root: Optional[TreeNode], low: float, up: float) -> bool:
            if not root:
                return True
            m = False
            if root.val > low and root.val < up:
                m = True
            l = is_valid_bst(root.left, low, root.val)
            r = is_valid_bst(root.right, root.val, up)
            return m & l & r
        return is_valid_bst(root, float('-inf'), float('+inf')) 

    # 可以使用中序遍历，判断是否是严格递增的也可以！
    # 这个思想也是非常好的，中序遍历二叉树的结果是严格递增的数组
    # 因此这种方法好处是：只需要一个变量记录前一个值就行！
    #pre_val = float('-inf')
    def isValidBST2(self, root: Optional[TreeNode]) -> bool:
        pre_val = float('-inf')
        def preorder(root: Optional[TreeNode]) -> bool:
            if not root:
                return True
            l = preorder(root.left)
            if root.val > pre_val:
                pre_val = root.val
            else:
                return False
            r = preorder(root.right)
            return l & r
            
        #pre_val = float('-inf')
        return preorder(root) 

        

if __name__ == "__main__":
    root = TreeNode(2, TreeNode(4), TreeNode(3))
    show = ShowTree()
    print(show.inorder(root))
    sol = Solution()
    ans = sol.isValidBST2(root)
    print(f"ans:{ans}")

