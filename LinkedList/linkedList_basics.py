'''
A program to create a LinkedList and traverse through it
1. Create a linkedlist
2. Add elements
3. traverse through it
'''


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linkedList:

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.length = 0

    def append_data(self, data):
        new_node = Node(data)
        if self.head.data is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next


ll = linkedList()
ll.append_data(3)
ll.append_data(4)
ll.append_data(5)

ll.print_list()



