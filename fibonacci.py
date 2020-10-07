def fibonacci(n):
    if n == 0:
        return "Incorrect input"
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
if __name__ == "__main__":
    value = int(input("Enter value: "))
    result = fibonacci(value)
    print(result)
