'''
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
示例 1：
输入：head = [4,2,1,3]
输出：[1,2,3,4]
示例 2：
输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]
示例 3：
输入：head = []
输出：[]
'''

from typing import Optional

def print_lst(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        


if __name__ == "__main__":
    print(f"k:2")
    h1 = ListNode(4, ListNode(2, ListNode(1, ListNode(3, ListNode(-5)))))
    print_lst(h1)    
    sol = Solution()
    ans = sol.sortList(h1)
    print_lst(ans)    
        
    
