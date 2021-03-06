class Node:
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
        self.prev = None  # Initialize prev as null


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
            else:
                temp = Node(value)
                p = self.head
                while p.next != None:
                    p = p.next
                temp.prev = p
                p.next = temp

    def insert_node(self, pos):
        value = input("Enter the node value:")
        temp = Node(value)
        p = self.head
        i = 1
        if pos == 1:
            temp.next = self.head
            self.head.prev = temp
            self.head = temp
        else:
            while (i < pos-1):
                i += 1
                p = p.next
            temp.prev = p
            temp.next = p.next
            p.next.prev = temp
            p.next = temp

    def delete_node(self, pos):
        p = self.head
        i = 1
        if pos == 1:
            self.head = self.head.next
            self.head.prev = None
            p = None
        else:
            while (i < pos-1):
                i += 1
                p = p.next
            temp = p.next
            p.next = temp.next
            temp.next.prev = p
            temp = None

    def reverse(self):
        curr = self.head
        prev = None
        while curr is not None:
            nxt = curr.next
            curr.prev = nxt
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


def printList(head):
    temp = head
    while (temp):
        print(temp.data, end="<=>")
        temp = temp.next
    print("NULL")


if __name__ == '__main__':
    nodes = int(input("Enter number of nodes: "))
    a = LinkedList(nodes)
    a.create_linked_list()
    # a.printList()
    # a.insert_node(4)
    # a.delete_node(3)
    head = a.reverse()
    printList(head)
