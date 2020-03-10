#Yanira Manzano
#3/9/2020
#Stack and Queues Assignment: Linked List

class ListNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return repr(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return str(nodes)

    def add_head(self, data):
        new_node = ListNode(data=data)
        if self.head is not None:
            new_node.next = self.head
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail = self.head

    def add_end(self, data):
        new_node = ListNode(data=data)
        self.tail.next = new_node
        self.tail = new_node

    def remove_head(self):
        new_node = self.head
        self.head = new_node.next
        return new_node.data

    def remove_end(self):
        current_node = self.head
        previous_node = self.head
        while current_node.next:
            previous_node = current_node
            current_node = current_node.next
        previous_node.next = None
        return current_node.data
