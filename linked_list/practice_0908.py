from calendar import c
from email.errors import NonPrintableDefect
from os import dup
import re

from nbformat import current_nbformat


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = new_node
    
    def prepend(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node
    
    def print_elements(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next
    
    def insertion_after_node(self, data, prev_node):
        if prev_node is None:
            print(f"No element macha")
            print()
            print()
            return
        
        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node
    
    def delete(self, key):
        curr_node = self.head

        if curr_node and curr_node.data == key:
            self.head = curr_node.next
            curr_node = None
            return
        
        prev = None
        while curr_node and curr_node.data != key:
            prev = curr_node
            curr_node = curr_node.next
        
        if curr_node is None:
            return
        
        prev.next = curr_node.next
        curr_node = None
    
    def delete_by_pos(self, pos):
        if self.head:
            curr_node = self.head
            count = 0
            if pos == 0:
                self.head = curr_node.next
                curr_node = None
                return
            
            prev = None
            while curr_node and count != pos:
                prev = curr_node
                curr_node = curr_node.next
                count += 1
            
            if curr_node is None:
                return
            
            prev.next = curr_node.next
            curr_node = None
    
    def reverse(self):
        curr_node = self.head
        prev = None
        while curr_node:
            nxt = curr_node.next
            curr_node.next = prev
            prev = curr_node
            curr_node = nxt
        self.head = prev
    
    def merged_list(self, llist):
        s = None
        p = self.head
        q = llist.head

        if p is None:
            return q
        
        if q is None:
            return p
        
        if p and q:
            if p.data < q.data:
                s = p
                p = p.next
            else:
                s = q
                q = q.next
            new_head  = s
        
        while p and q:
            if p.data < q.data:
                s.next = p
                s = p
                p = p.next
            else:
                s.next = q
                s = q
                q = q.next
        if not p:
            s.next = q
        if not q:
            s.next = p
        
        self.head = new_head
        return self.head
    
    def remove_duplicates(self):
        cur = self.head
        prev = None
        dup_values = {}

        while cur:
            if cur.data in dup_values:
                prev.next = cur.next
                cur = None
            else:
                dup_values[cur.data] = 1
                prev = cur
            cur = prev.next
        



llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(4)
llist.append(7)
llist.print_elements()
print()
llist2 = LinkedList()
llist2.append(3)
llist2.append(5)
llist2.append(6)
llist2.append(8)
llist2.append(8)
llist2.append(8)
llist2.print_elements()
print()

llist2.remove_duplicates()
llist2.print_elements()
print()

llist.merged_list(llist2)
llist.print_elements()
print()


