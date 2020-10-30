from singlyLinkedList import LinkedList, Node


a = LinkedList(8)
head = a.create_linked_list()


def delete_duplicate(head):
    temp = head
    while temp.next != None:
        after_next = temp.next.next
        if temp.data == temp.next.data:
            temp.next = None
            temp.next = after_next
        temp = temp.next
    return head

def printList(head):
    temp = head
    while (temp):
        print(temp.data, end="=>")
        temp = temp.next
    print("NULL")


head = delete_duplicate(head)
printList(head)
