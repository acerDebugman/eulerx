'''
请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
实现 LRUCache 类：
LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。
示例：
输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]
解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4
'''

from typing import Optional,List
from print_tools import print_lst

class ListNode:
    def __init__(self, key=0, val=0, pre=None, next=None):
        self.key = key 
        self.val = val
        self.pre = pre
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.data = {}
        self.dummyh = ListNode()
        self.tail = self.dummyh

    def get(self, key: int) -> int:
        if key in self.data:
            node = self.data[key]
            if node.next:
                node.next.pre = node.pre
                node.pre.next = node.next
                node.pre = node.next = None

                node.pre = self.tail 
                self.tail.next = node
                self.tail = self.tail.next
            
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.data:
            node = ListNode(key, value)
            self.data[key] = node

            node.pre = self.tail
            self.tail.next = node
            self.tail = self.tail.next 
        else:
            node = self.data[key]
            node.val = value
            if node.next:
                node.next.pre = node.pre
                node.pre.next = node.next
                node.pre = node.next = None
            
                node.pre = self.tail
                self.tail.next = node
                self.tail = self.tail.next 
        
        if len(self.data) > self.cap:
            oldnode = self.dummyh.next
            self.dummyh.next = oldnode.next
            self.dummyh.next.pre = self.dummyh

            oldnode.pre = oldnode.next = None
            del self.data[oldnode.key]
        
from collections import OrderedDict

class LRUCache2:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key) 
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)


if __name__ == "__main__":
    obj = LRUCache(2)
    obj.put(2,1)
    obj.put(2,2)
    v = obj.get(2)
    print(f"{v}")

    obj.put(1,1)
    obj.put(4,1)
    v = obj.get(2)
    print(f"{v}")

    '''
    obj.put(4,4)
    v = obj.get(1)
    print(f"{v}")
    v = obj.get(3)
    print(f"{v}")
    v = obj.get(4)
    print(f"{v}")
    '''

