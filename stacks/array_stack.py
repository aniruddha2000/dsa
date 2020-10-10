def create_stack():
    stack = []
    return stack

def isEmptyStack(stack):
    return len(stack) == 0

def push(stack, data):
    stack.append(data)
    print("Pushed : " + data)

def pop(stack):
    if isEmptyStack(stack):
        print("stack is empty")
    print("Removed : " + stack.pop())

def delete_stack(stack):
    stack.clear()

if __name__ == "__main__":
    stack = create_stack()
    push(stack, str(10))
    push(stack, str(20))
    push(stack, str(30))
    pop(stack)
    delete_stack(stack)
    print(stack)
