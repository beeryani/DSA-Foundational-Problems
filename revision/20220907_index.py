from calendar import c
from nbformat import current_nbformat


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next
    
    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node
    
    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Node not found")
            return
        
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    
    def delete_by_value(self, key):
        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return
        
        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next
        
        if cur_node is None:
            return
        
        prev.next = cur_node.next
        cur_node = None
    
    def delete_by_position(self, pos):
        if self.head:
            cur_node = self.head
            if pos == 0:
                self.head = cur_node.next
                cur_node = None
                return
            
            prev = None
            count = 0
            while cur_node and count != pos:
                prev = cur_node
                cur_node = cur_node.next
                count += 1
            
            if cur_node is None:
                return
            
            prev.next = cur_node.next
            cur_node = None
    
    def length(self):
        cur_node = self.head
        count = 0
        while cur_node:
            cur_node = cur_node.next
            count += 1
        print(count)
    
    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev
    
    def swap_node(self, key_1, key_2):

        if key_1 == key_2:
            return
        
        prev_1 = None
        curr_1 = self.head
        if curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next
        
        prev_2 = None
        curr_2 = self.head
        if curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next
        
        if not curr_1 and not curr_2:
            return
        
        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2
        
        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1
        
        curr_1.next, curr_2.next = curr_2.next, curr_1.next
    
    def remove_duplicates(self):
        curr_node = self.head
        prev = None
        dup_values = {}

        while curr_node:
            if curr_node.data in dup_values:
                prev.next = curr_node.next
                curr_node = None
            else:
                dup_values[curr_node.data] = 1
                prev = curr_node
            curr_node = prev.next

    def merge_sorted(self, llist):

        p = self.head
        q = llist.head
        s = None

        if not p:
            return q

        if not q:
            return p

        if p and q:
            if p.data < q.data:
                s = p
                p = p.next
            else:
                s = q
                q = q.next
            new_head = s
            



llist = LinkedList()
llist.append("@")
llist.append("@23")
llist.append("3")
llist.append("3")
llist.prepend("3")
llist.print_list()
llist.remove_duplicates()
print()
llist.print_list()
