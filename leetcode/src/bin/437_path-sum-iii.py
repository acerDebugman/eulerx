'''
给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。
路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
示例 1：
输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
输出：3
解释：和等于 8 的路径有 3 条，如图所示。
示例 2：
输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：3
'''

from typing import Optional,List,Dict
from print_tools import ShowTree
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 本质上前缀求和和数组的前缀求和是一样的，只是数组是顺序遍历，而树结构是分前，中，后遍历
    # 
    def pathSum2(self, root: Optional[TreeNode], targetSum: int) -> int:
        # 这一步不需要
        def prefix_sum(root: Optional[TreeNode], s:int, sum_node: Dict):
            if not root:
                return 
            cur_pre_v = root.val + s
            sum_node[cur_pre_v] = root
            prefix_sum(root.left, cur_pre_v, sum_node)
            prefix_sum(root.right, cur_pre_v, sum_node)
            
        #sum_node 保存前缀是k的次数，比如1-0-2 这样的单链，前缀和是1的有1，1-0; 前缀和是2的有0,0-2 ，所以要记录次数
        def path_sum(root: Optional[TreeNode], psum: int, target:int, sum_node: Dict) -> int:
            if not root:
                return 0
            curv = psum+root.val
            cnt = sum_node[curv - target]

            sum_node[curv]+=1
            l = path_sum(root.left, curv, target, sum_node)
            r = path_sum(root.right, curv, target, sum_node)
            sum_node[curv]-=1
            #print(l,r,curv-target)
            return cnt + l + r
        
        sum_node = collections.defaultdict(int)
        sum_node[0] = 1
        return path_sum(root, 0, targetSum, sum_node)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(root:Optional[TreeNode], sumv, target, ans: TreeNode):
            if not root:
                return 
            if sumv + root.val == target :
                ans.val+=1
            dfs(root.left, sumv+root.val, target, ans)
            dfs(root.right, sumv+root.val, target, ans)

        def preorder(root, sumv, target, ans):
            if not root:
                return 
            
            dfs(root, sumv, target, ans)
            preorder(root.left, sumv, target, ans)
            preorder(root.right, sumv, target, ans)
        
        ans = TreeNode(0)
        preorder(root, 0, targetSum, ans)
        return ans.val

    
if __name__ == "__main__":
    #root = TreeNode(3, TreeNode(2), TreeNode(5, TreeNode(4), TreeNode(6)))
    root = TreeNode(0, TreeNode(1), TreeNode(1))
    #root = TreeNode(1)
    show = ShowTree()
    print(show.inorder(root))
    print(show.levelorder(root))
    sol = Solution()
    ans = sol.pathSum2(root, 0)
    print(f"ans:{ans}")
    

   
