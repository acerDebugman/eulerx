from typing import Optional,List
import collections

def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

def print_lst(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ShowTree:
    def build_tree_from_level_order_lst(self, lst) -> Optional[TreeNode]:
        if not lst:
            return None
        root = TreeNode(lst[0])
        q = collections.deque()
        q.append((root,0))
        while q:
            node,n = q.popleft()
            if node:
                l, r = 2*n+1, 2*n+2
                if l < len(lst) and lst[l]:
                    lnode = TreeNode(lst[l])
                    node.left = lnode
                    q.append((lnode, l))
                if r < len(lst) and lst[r]:
                    rnode = TreeNode(lst[r])
                    node.right = rnode
                    q.append((rnode, r))
        return root

    def levelorder(self, root: Optional[TreeNode]) -> List[int]:
        def levelorder(root: Optional[TreeNode], ans: List[int]):
            if not root:
                return
            q = collections.deque()     
            q.append(root)
            while q:
                e = q.popleft()
                ans.append(e.val) if e else ans.append(None)
                if e:
                    q.append(e.left)
                    q.append(e.right)

        ans = []
        levelorder(root, ans)
        idx = len(ans)
        for i in [n for n in enumerate(ans)][::-1]:
            if i[1]:
                idx = i[0] 
                break
        return ans[:idx+1]

    def inorder(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(root: Optional[TreeNode], ans: List[int]):
            if not root:
                return
            if root.left:
                inorder(root.left, ans)
            ans.append(root.val)
            if root.right:
                inorder(root.right, ans)

        ans = []
        inorder(root, ans)
        return ans

    def preorder(self, root: Optional[TreeNode]) -> List[int]:
        def _preorder(root: Optional[TreeNode], ans: List[int]):
            if not root:
                return
            ans.append(root.val)
            if root.left:
                _preorder(root.left, ans)
            if root.right:
                _preorder(root.right, ans)

        ans = []
        _preorder(root, ans)
        return ans        

    def postorder(self, root: Optional[TreeNode]) -> List[int]:
        def _postorder(root: Optional[TreeNode], ans: List[int]):
            if not root:
                return 
            if root.left:
                _postorder(root.left, ans)
            if root.right:
                _postorder(root.right, ans)
            ans.append(root.val)
        
        ans = []
        _postorder(root, ans)
        return ans


class ShowList:
    def showlist(lst):
        for row in lst:
            print(row)
        

