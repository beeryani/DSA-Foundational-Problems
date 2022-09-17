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
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node
    
    def print_list(self):
        if self.head:
            curr_node = self.head
            while curr_node:
                print(curr_node.data)
                curr_node = curr_node.next
    
    def prepend(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def insert_after_node(self, prev_data, new_data):
        new_node = Node(new_data)
        
        if self.head:
            curr_node = self.head

            while curr_node and curr_node.data != prev_data:
                curr_node = curr_node.next
            
            if curr_node is None:
                return
            
            if curr_node.data == prev_data:
                new_node.next = curr_node.next
                curr_node.next = new_node
    
    def delete_by_value(self, data_to_be_deleted):  
        curr_node = self.head

        if curr_node and curr_node.data == data_to_be_deleted:
            self.head = curr_node.next
            curr_node = None
            return
        
        prev = None

        while curr_node and curr_node.data != data_to_be_deleted:
            prev = curr_node
            curr_node = curr_node.next

        if curr_node is None: 
            return print(f'{data_to_be_deleted} not found, try with a valid entry')

        prev.next = curr_node.next
        curr_node = None
                



llist = LinkedList()
llist.append("8")
llist.append("@@@@")
llist.append("@@@@")
llist.insert_after_node("@@@@", "6")
llist.delete_by_value("6")
llist.print_list()
    