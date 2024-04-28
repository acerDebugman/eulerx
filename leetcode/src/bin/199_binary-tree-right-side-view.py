'''
给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
示例 1:
输入: [1,2,3,null,5,null,4]
输出: [1,3,4]
示例 2:
输入: [1,null,3]
输出: [1,3]
示例 3:
输入: []
输出: []
'''

from typing import Optional,List
from print_tools import ShowTree
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 思路2：一层保存一个队列就行，然后只取最后一个元素即可
    def rightSideView2(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        q = deque()
        q.append([root])
        while q:
            level = []
            lst = q.popleft()
            for i in range(len(lst)):
                if lst[i].val:
                    r = lst[i].val
                if lst[i].left:
                    level.append(lst[i].left)
                if lst[i].right:
                    level.append(lst[i].right)
            if level:
                q.append(level)
            ans.append(r)
        return ans

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def level_order(root, ans:List):
            q = deque()
            ans.append(root.val)
            q.append(root)
            q.append(None)
            while q:
                e = q.popleft()
                if e is None and len(q) > 0:
                    ans.append(q[-1].val)
                    q.append(None)
                if e and e.left:
                    q.append(e.left)
                if e and e.right:
                    q.append(e.right)
        ans = []
        level_order(root, ans)
        return ans


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(2), TreeNode(5, TreeNode(4), TreeNode(6)))
    #root = TreeNode(3, TreeNode(2))
    show = ShowTree()
    print(show.inorder(root))
    sol = Solution()
    ans = sol.rightSideView2(root)
    print(f"ans:{ans}")
    

   
