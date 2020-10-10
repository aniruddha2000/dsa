class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SymolBalance:
    def __init__(self):
        self.head = None

    def isEmptyStack(self):
        return True if self.head is None else False

    def push(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def pop(self):
        if (self.isEmptyStack()):
            print("No symbols")
        p = self.head
        self.head = self.head.next
        return p.data

    def isSymbolBalanced(self, expr):
        for char in expr:
            if char in ['(', '{', '[']:
                self.push(char)
            else:
                if self.isEmptyStack():
                    return False
                current_char = self.pop()
                if current_char == '(':
                    if char != ')':
                        return False
                if current_char == '{':
                    if char != '}':
                        return False
                if current_char == '[':
                    if char != ']':
                        return False
        if not self.isEmptyStack():
            return False
        return True


if __name__ == "__main__":
    expr = "{()}[]"
    a = SymolBalance()
    if a.isSymbolBalanced(expr):
        print("Balanced")
    else :
        print("Not Balanced")
