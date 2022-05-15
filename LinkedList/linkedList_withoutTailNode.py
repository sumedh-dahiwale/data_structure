''' Attempting to create a linked list and append elements without using self.tail node '''


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self):
        self.head = Node()
    
    def append_ele(self, data, temp=None):
        new_node = Node(data)
        if self.head.data is None:
            self.head = new_node
            temp = self.head
        else:
            temp.next = new_node
            
            
        
        
