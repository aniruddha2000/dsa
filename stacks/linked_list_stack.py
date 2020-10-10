class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def isEmptyStack(self):
        return True if self.head is None else False

    def push(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp
        print("Pushed : " + data)

    def pop(self):
        if (self.isEmptyStack()):
            print("Empty Stack.")
        p = self.head
        self.head = self.head.next
        print("Popped : " + p.data)
        p = None


if __name__ == "__main__":
    stack = Stack()
    stack.push(str(5))
    stack.push(str(10))
    stack.push(str(20))
    stack.pop()
