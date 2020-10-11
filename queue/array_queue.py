class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.front = self.rear = -1

    def enQueue(self, data):
        # if queue is full
        if ((self.rear == self.size - 1) and (self.front == 0)):
            print("Queue is full.")

        # if queue is empty
        elif (self.front == -1):
            self.front = self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data

    def deQueue(self):
        if (self.front == -1):
            print("Queue is empty")
        elif (self.front == self.rear):
            print("Removed : " + str(self.queue[self.front]))
            self.queue[self.front] = None
            self.front = self.rear = -1
        else:
            print("Removed : " + str(self.queue[self.front]))
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.size

    def display(self):

        # condition for empty queue
        if(self.front == -1):
            print("Queue is Empty")

        elif (self.rear >= self.front):
            print("Elements in the circular queue are:",
                  end=" ")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()

        else:
            print("Elements in Circular Queue are:",
                  end=" ")
            for i in range(self.front, self.size):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")
            print()

        if ((self.rear + 1) % self.size == self.front):
            print("Queue is Full")


if __name__ == "__main__":
    queue = Queue(5)
    queue.deQueue()
    queue.enQueue(5)
    queue.enQueue(6)
    queue.enQueue(6)
    queue.enQueue(6)
    queue.enQueue(6)
    queue.enQueue(9)
    queue.display()
