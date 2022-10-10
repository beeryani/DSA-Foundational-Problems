# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = head
        if head is None:
            return 0
        
        length = 0
        prev = None
        while head:
            prev = head
            head = head.next
            length += 1
        
        count = 0
        new_prev = None
        if length%2 != 0:
            while count < (length)//2:
                new_prev = new_head
                new_head = new_head.next
                count += 1
        else:
            while count < (length + 1)//2:
                new_prev = new_head
                new_head = new_head.next
                count += 1
            
        
        self.head = new_head
        return self.head
        
            
            
            
            
        