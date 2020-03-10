#Yanira Manzano
#3/9/2020
#Stack and Queues: Stack Script

from Linkedlists import Node

class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head == None:
            return None
        removed = self.head.data
        self.head = self.head.next
        return removed


    def depict(self):
        list = []
        current = self.head
        while current is not None:
            if current.data is not None:
                list.append(current.data)
            current = current.next
        print(list)


mylist = Stack()
mylist.push(3)
mylist.push(5)
mylist.push(7)
mylist.push(9)
mylist.push(11)
mylist.depict()
mylist.pop()
mylist.depict()
