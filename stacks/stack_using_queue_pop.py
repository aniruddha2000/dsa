from queue import Queue

class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        self.current_size = 0

    def push(self, data):
        self.q1.put(data)
        self.current_size += 1

    def pop(self):
        if self.q1.empty():
            print("Empty stack")
        while self.q1.qsize() != 1:
            self.q2.put(self.q1.queue[0])
            self.q1.get()
            # self.current_size -= 1
        print("Removed : " + str(self.q1.get()))
        self.current_size -= 1
        self.q1, self.q2 = self.q2, self.q1


if __name__ == "__main__":
    stack = Stack()
    stack.push(5)
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    stack.pop()
    stack.pop()
    stack.pop()
