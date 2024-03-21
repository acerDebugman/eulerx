from typing import Optional,List

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
    def inorder(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def inorder(root: Optional[TreeNode], ans: List[int]):
            if not root:
                return
            if root.left:
                inorder(root.left, ans)
            ans.append(root.val)
            if root.right:
                inorder(root.right, ans)

        inorder(root, ans)
        return ans

