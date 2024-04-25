'''
给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵平衡二叉搜索树。

输入：nums = [-10,-3,0,5,9]
输出：[0,-3,9,-10,null,5]
解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：

输入：nums = [1,3]
输出：[3,1]
解释：[1,null,3] 和 [3,1] 都是高度平衡二叉搜索树。
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
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def inorder_gen(nums: List[int], l: int, r: int) -> Optional[TreeNode]:
            if l > r: 
                return None
            if  l == r:
                return TreeNode(nums[l])
            m = int((l+r)/2)
            node = TreeNode(nums[m])
            node.left = inorder_gen(nums, l, m-1) 
            node.right = inorder_gen(nums, m+1, r) 
            return node
        return inorder_gen(nums, 0, len(nums)-1)


if __name__ == "__main__":
    show = ShowTree()
    nums = [-10,-3,0,5,9]
    sol = Solution()
    ans = sol.sortedArrayToBST(nums)
    print(show.inorder(ans))

    #root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, None, TreeNode(5)))
    show = ShowTree()
    nums = [0,9]
    sol = Solution()
    ans = sol.sortedArrayToBST(nums)
    print(show.inorder(ans))


