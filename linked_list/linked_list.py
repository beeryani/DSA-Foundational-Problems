'''
practice Linked List
'''

from calendar import c
from hashlib import new


class Node:
    def __init__(self,data):
        self.head = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.head)
            cur_node = cur_node.next
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = new_node
    
    def prepend(self, data):
        if self.head:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
    
    def insert_after_element(self, prev_node, data):
        if not prev_node:
            print("Ja na re bhai")
            return

        new_node = Node(data)
        
        new_node.next = prev_node.next
        prev_node.next = new_node
    
    def delete(self, key):
        curr_node = self.head

        if curr_node and curr_node == key:
            self.head = curr_node.next
            curr_node = None
            return

        prev = None
        while curr_node and curr_node.head != key:
            prev = curr_node
            curr_node = curr_node.next
        
        if curr_node is None:
            return

        prev.next = curr_node.next
        curr_node = None
    
    def delete_position(self, pos):
        if self.head:
            curr_node = self.head
            if pos == 0:
                self.head = curr_node.next
                curr_node = None
                return
            
            prev = None
            count = 0
            while curr_node and count != pos:
                prev = curr_node
                curr_node = curr_node.next
                count += 1

            if curr_node is None:
                return

            prev.next = curr_node.next
            curr_node = None
    
    def length(self):
        count = 0
        curr_node = self.head
        while curr_node:
            curr_node = curr_node.next
            count += 1
        return count


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.prepend(1)
llist.insert_after_element(llist.head, "R")
llist.print_list()
print()
print(llist.length())
print()
llist.delete("R")
llist.print_list()
print()
llist.delete_position(0)
llist.print_list()
print()
print(llist.length())