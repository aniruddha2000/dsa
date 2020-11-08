class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enQueue(self, data):
        self.s1.append(data)

    def deQueue(self):
        if len(self.s1) == 0 and len(self.s2) == 0:
            print("Empty Queue")
            return
        elif len(self.s2) == 0 and len(self.s1) > 0:
            while len(self.s1) != 0:
                temp = self.s1.pop()
                self.s2.append(temp)
            return self.s2.pop()
        else:
            return self.s2.pop()

if __name__ == "__main__":
    q = Queue()
    q.enQueue(5)
    print(q.deQueue())
    q.enQueue(10)
    q.enQueue(15)
    print(q.deQueue())
    print(q.deQueue())
