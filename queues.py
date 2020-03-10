#Yanira Manzano
#3/9/2020
#Stack and Queues: Queues Script

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        if self.tail is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

    def dequeue(self):
        if self.head is None:
            return None
        else:
            last_data = self.head.data
            self.head = self.head.next
            return last_data

    def depict(self):
        list = []
        current = self.head
        while current is not None:
            if current.data is not None:
                list.append(current.data)
            current = current.next
        print(list)

myqueue = Queue()

myqueue.enqueue(4)
myqueue.enqueue(8)
myqueue.enqueue(12)
myqueue.enqueue(16)
myqueue.depict()
myqueue.dequeue()
myqueue.depict()
myqueue.enqueue(20)
myqueue.depict()
