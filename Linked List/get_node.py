from singlyLinkedList import LinkedList, Node


a = LinkedList(8)
head = a.create_linked_list()


def getNode(head, pos):
    p = head
    count = 0
    while head != None:
        head = head.next
        if count < pos+1:
            count += 1
        else:
            p = p.next
    return p.data

print(getNode(head, 4))
