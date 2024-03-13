'''
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
示例 1：
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
示例 2：
输入：head = [1], n = 1
输出：[]
示例 3：
输入：head = [1,2], n = 1
输出：[1]
'''


from print_tools import print_linked_list
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd_x(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = dummy_head = ListNode(next=head)
        while n:
            fast = fast.next
            n -= 1
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        return dummy_head.next

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next and n == 1:
            return None
        slow = fast = head
        while n > 0:
            fast = fast.next
            n -= 1
        if not fast:
            return head.next

        pre = slow
        while fast:
            fast = fast.next
            pre = slow
            slow = slow.next
         
        if slow and slow.next:
            pre.next = slow.next
        else:
            pre.next = None
         
        return head


if __name__ == "__main__":
    h1 = ListNode(1, ListNode(2, ListNode(4)))
    print_linked_list(h1);
    s = Solution();
    ans = s.removeNthFromEnd(h1, 2)
    print_linked_list(ans);

    h1 = ListNode(1, ListNode(2, ListNode(4, ListNode(3))))
    print_linked_list(h1);
    s = Solution();
    ans = s.removeNthFromEnd(h1, 4)
    print_linked_list(ans);

    h1 = ListNode(1)
    print_linked_list(h1);
    s = Solution();
    ans = s.removeNthFromEnd(h1, 1)
    print_linked_list(ans);
    pass
