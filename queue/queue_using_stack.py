class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enQueue(self, data):
        while len(self.s1) != 0:
            self.s2.append(self.s1[-1])
            self.s1.pop()
        self.s1.append(data)
        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()


    def deQueue(self):
        if len(self.s1) == 0:
            print("Queue is empty.")
        print("Removed : " + str(self.s1[-1]))
        self.s1.pop()


if __name__ == "__main__":
    queue = Queue()
    queue.enQueue(5)
    queue.enQueue(10)
    queue.enQueue(6)
    queue.deQueue()
    queue.deQueue()
