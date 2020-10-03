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
            value = input("Enter the {} node:".format(node))
            if self.head == None:
                self.head = Node(value)
            else:
                temp = Node(value)
                p = self.head
                while p.next != None:
                    p = p.next
                p.next = temp

    def insert_node(self, pos):
        value = input("Enter the node value:")
        temp = Node(value)
        p = self.head
        i = 1
        if pos == 1:
            temp.next = p
            p = temp
            # p = temp
        else:
            while (i < pos-1):
                i += 1
                p = p.next
            temp.next = p.next
            p.next = temp

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    nodes = int(input("Enter number of nodes: "))
    a = LinkedList(nodes)
    a.create_linked_list()
    a.printList()
    a.insert_node(2)
    a.printList()
