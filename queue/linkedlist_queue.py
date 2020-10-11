class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front == None

    def enQueue(self, data):
        temp = Node(data)
        if self.front == None:
            self.rear = self.front = temp
        self.rear.next = temp
        self.rear = temp

    def deQueue(self):
        if self.isEmpty():
            print("Empty Queue")
        temp = self.front
        self.front = temp.next
        print("Removed : " + str(temp.data))
        temp = None
        if (self.front == None):
            self.rear = None

    def display(self):
        temp = self.front
        while temp:
            print(temp.data, end="=>")
            temp = temp.next
        print("NULL")

if __name__ == "__main__":
    queue = Queue()
    queue.enQueue(5)
    queue.enQueue(10)
    queue.enQueue(6)
    # queue.deQueue()
    # queue.deQueue()
    queue.display()
