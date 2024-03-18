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
    def merge2lst(self, h1: Optional[ListNode], h2: Optional[ListNode]) -> Optional[ListNode]:
        ans = tail = ListNode()
        while h1 and h2:
            if h1.val < h2.val:
                tail.next = h1
            else:
                tail.next = h2
            h1 = h1.next
            h2 = h2.next
            tail = tail.next
        
        if h1:
            tail.next = h1
        if h2:
            tail.next = h2
        return ans.next

    # nlogn
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def dfs():
            pass
        
        pass
    #O(n^2)
    def sortList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        nxth = self.sortList(head.next)
        dummyh,p = ListNode(0,nxth),nxth
        pre = dummyh
        while p and head.val > p.val:
            pre = p 
            p = pre.next
        head.next = p
        pre.next = head
            
        return dummyh.next


if __name__ == "__main__":
    print(f"k:2")
    h1 = ListNode(4, ListNode(2, ListNode(1, ListNode(3, ListNode(-5)))))
    print_lst(h1)    
    sol = Solution()
    ans = sol.sortList(h1)
    print_lst(ans)    
        
    
