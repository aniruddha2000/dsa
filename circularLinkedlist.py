class Node:
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


class LinkedList:
    def __init__(self, nodes):
        self.head = None
        self.nodes = nodes

    def create_linked_list(self):
        for node in range(1, nodes+1):
            # value = input("Enter the {} node:".format(node))
            value = node
            if self.head == None:
                self.head = Node(value)
                self.head.next = self.head
            else:
                temp = Node(value)
                p = self.head
                while p.next != self.head:
                    p = p.next
                p.next = temp
                temp.next = self.head

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end="=>")
            temp = temp.next
            if temp == self.head:
                break


if __name__ == '__main__':
    nodes = int(input("Enter number of nodes: "))
    a = LinkedList(nodes)
    a.create_linked_list()
    a.printList()
