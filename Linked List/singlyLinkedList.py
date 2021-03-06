class Node:
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


class LinkedList:
    def __init__(self, nodes):
        self.head = None
        self.nodes = nodes

    def create_linked_list(self):
        for node in range(1, self.nodes+1):
            # value = input("Enter the {} node:".format(node))
            value = node
            if self.head == None:
                self.head = Node(value)
            else:
                temp = Node(value)
                p = self.head
                while p.next != None:
                    p = p.next
                p.next = temp
        return self.head

    def insert_node(self, pos):
        value = input("Enter the node value:")
        temp = Node(value)
        p = self.head
        i = 1
        if pos == 1:
            temp.next = self.head
            self.head = temp
        else:
            while (i < pos-1):
                i += 1
                p = p.next
            temp.next = p.next
            p.next = temp

    def delete_node(self, pos):
        p = self.head
        i = 1
        if pos == 1:
            self.head = self.head.next
            p = None
        else:
            while (i < pos-1):
                i += 1
                p = p.next
            temp = p.next
            p.next = p.next.next
            temp = None

    def reverse_list(self):
        prev = None
        curr = self.head
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev


    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end="=>")
            temp = temp.next
        print("NULL")


if __name__ == '__main__':
    nodes = int(input("Enter number of nodes: "))
    a = LinkedList(nodes)
    a.create_linked_list()
    a.printList()
    # a.insert_node(7)
    # a.delete_node(3)
    a.reverse_list()
    a.printList()
