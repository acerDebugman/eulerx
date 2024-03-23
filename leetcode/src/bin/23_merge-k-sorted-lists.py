'''
给你一个链表数组，每个链表都已经按升序排列。
请你将所有链表合并到一个升序链表中，返回合并后的链表。
示例 1：
输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6
示例 2：
输入：lists = []
输出：[]
示例 3：
输入：lists = [[]]
输出：[]
'''

from typing import Optional,List
from print_tools import print_lst

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(lists: List[Optional[ListNode]], start, end) -> Optional[ListNode]:
            if len(lists) == 0:
                return []
            if start == end:
                return lists[start]
            mid = start + int((end - start)/2)
            h1 = merge(lists, start, mid) 
            h2 = merge(lists, mid+1, end)
            ans = tail = ListNode(0)
            while h1 and h2:
                if h1.val < h2.val:
                    tail.next = h1
                    h1 = h1.next
                else:
                    tail.next = h2
                    h2 = h2.next
                tail = tail.next
            tail.next = h1 if h1 else h2
            return ans.next
        
        return merge(lists, 0, len(lists) - 1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergelist(l1, l2) -> Optional[ListNode]:
            if not l1:
                return l2
            if not l2:
                return l1
            if l1.val < l2.val:
                l1.next = mergelist(l1.next, l2)
                return l1
            else:
                l2.next = mergelist(l1, l2.next)
                return l2

        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        while len(lists) > 1:
            newlst = mergelist(lists[0], lists[1])
            del lists[:2]
            lists.append(newlst)
        return lists[0] 

                
    def mergeKLists2(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergelist(list1,list2):
            if not list1:
                return list2
            if not list2:
                return list1
            if list1.val <= list2.val:
                list1.next = mergelist(list.next,list2)
                return list1
            else:
                list2.next = mergelist(list1,list2.next)
                return list2# Definition for singly-linked list.

    def mergeKLists_x(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergelist(list1,list2):
            if not list1:
                return list2
            if not list2:
                return list1
            if list1.val <= list2.val:
                list1.next = mergelist(list1.next,list2)
                return list1
            else:
                list2.next = mergelist(list1,list2.next)
                return list2

        if lists == []:
            return None
        if len(lists) == 1:
            return lists[0]
        while len(lists) > 1:
            new_merge = mergelist(lists[0],lists[1])
            del lists[:2]
            lists.append(new_merge)
        return lists[0]
        

if __name__ == "__main__":
    h1 = ListNode(1, ListNode(5, ListNode(9)))
    h2 = ListNode(2, ListNode(3, ListNode(4, ListNode(7, ListNode(22)))))
    lst = [h1,h2]
    print_lst(lst[0])
    print_lst(lst[1])
    sol = Solution()
    ans = sol.mergeKLists(lst)
    print_lst(ans)    

    lst = []
    sol = Solution()
    ans = sol.mergeKLists(lst)
    print_lst(ans)    

    
