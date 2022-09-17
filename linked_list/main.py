'''
Node has two components
1. Data
2. Next

Main advantage of Linked Lists is insertion and deletion in O(1)
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    

class LinkedList:
    def __init__(self):
        self.head = None
    
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def prepend(self,data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node
    
    def insertion_after_node(self,data, previous_node):
        if not previous_node:
            print("no node found")
            return
        
        new_node = Node(data)

        new_node.next = previous_node.next
        previous_node.next = new_node
    
    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node does not exist.")
            return
        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        cur_node = self.head

        if cur_node and cur_node == key:
            self.head = cur_node.next
            cur_node = None
            return
        
        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next
        
        prev.next = cur_node.next
        cur_node = None
    
    def delete_at_pos(self, pos):
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
    
    def swap(self, key1, key2):
        prev1 = None
        curr1 = self.head

        while curr1 and curr1.data != key1:
            prev1 = curr1
            curr1 = curr1.next

        prev2 = None
        curr2 = self.head
        
        while curr2 and curr2.data != key2:
            prev2 = curr2
            curr2 = curr2.next
        
        if not curr1 or not curr2:
            return

        if prev1:
            prev1.next = curr2
        else:
            self.head = curr2
        
        if prev2:
            prev2.next = curr1
        else:
            self.head = curr1
        
        curr2.next, curr1.next = curr1.next, curr2.next
    
    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.prepend("E")
llist.insertion_after_node("D", llist.head )
llist.print_list()
# llist.delete_node("A")
print()
llist.delete_at_pos(1)

llist.print_list()
print()

llist.swap("E", "C")
llist.print_list()
print()
llist.swap("E", "A")
llist.print_list()
print()

llist.reverse()
llist.print_list()
print()

