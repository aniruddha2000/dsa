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

    def insert_node(self, pos):
        value = input("Enter the node value:")
        temp = Node(value)
        p = self.head
        i = 1
        if pos == 1:
            while p.next != self.head:
                p = p.next
            temp.next = self.head
            self.head = temp
            p.next = self.head
        else:
            while (i < pos-1):
                i += 1
                p = p.next
            if pos == nodes+1:
                p.next = temp
                temp.next = self.head
            temp.next = p.next
            p.next = temp

    def delete_node(self, pos):
        p = self.head
        temp = self.head
        i = 1
        if pos == 1:
            while p.next != self.head:
                p = p.next
            p.next = self.head.next
            self.head = self.head.next
            temp = None
        else:
            while (i < pos-1):
                i += 1
                p = p.next
            # print(p.data)
            temp = p.next
            if pos == nodes+1:
                p.next = self.head
                temp = None
            p.next = p.next.next
            temp = None

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
    # a.insert_node(6)
    a.delete_node(3)
    a.printList()
