from singlyLinkedList import LinkedList, Node


a = LinkedList(4)
head1 = a.create_linked_list()
b = LinkedList(2)
head2 = b.create_linked_list()


def merge_list(head1, head2):
    dummy = Node(0)
    p = dummy
    while True:
        if head1 is None:
            p.next = head2
            break
        if head2 is None:
            p.next = head1
            break

        if head1.data <= head2.data:
            p.next = head1
            head1 = head1.next
        else:
            p.next = head2
            head2 = head2.next
        p = p.next
    return dummy.next

def printList(head):
    temp = head
    while (temp):
        print(temp.data, end="=>")
        temp = temp.next
    print("NULL")

a = merge_list(head1, head2)
printList(a)
