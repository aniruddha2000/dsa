def combination(dialpad, input, index, res=""):
    if index == -1:
        print(res, end=" ")
        return
    digit = input[index]
    length = len(dialpad[digit])
    for i in range(length):
        combination(dialpad, input, index-1, dialpad[digit][i]+res)

dialpad = [
    [],
    [],
    ['A', 'B', 'C'],
    ['D', 'E', 'F'],
    ['G', 'H', 'I'],
    ['J', 'K', 'L'],
    ['M', 'N', 'O'],
    ['P', 'Q', 'R', 'S'],
    ['T', 'U', 'V'],
    ['W', 'X', 'Y', 'Z']
]
input = [2, 3, 4]
combination(dialpad, input, len(input)-1)
