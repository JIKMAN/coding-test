## source : https://leetcode.com/problems/reverse-nodes-in-k-group/

import re
from typing import Optional


head = [1,2,3,4,5]
k = 2

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        sentinel_head = ListNode()
        sentinel_head.next = head
        Tail = sentinel_head
        while True:
            p = Tail.next
            for _ in range(k):
                if p == None:
                    return sentinel_head.next
                p = p.next
            prev, curr = None, Tail.next
            for i in range(k):
                curr.next, prev, curr = prev, curr, curr.next
            Tail.next.next, Tail.next, Tail = curr, prev, Tail.next

        return sentinel_head.next


print(Solution.reverseKGroup(head, k))