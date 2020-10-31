from singlyLinkedList import LinkedList, Node


a = LinkedList(4)
head1 = a.create_linked_list()
b = LinkedList(2)
head2 = b.create_linked_list()


def printList(head):
    temp = head
    while (temp):
        print(temp.data, end="=>")
        temp = temp.next
    print("NULL")


def findMergeNode(head1, head2):
    head1_curr = head1
    head2_curr = head2
    while head1_curr.next != None:
        head1_curr = head1_curr.next
    head1_curr.next = head2
    while head2_curr.next != None:
        head2_curr = head2_curr.next
    head2_curr.next = head1
    printList(head1)
    printList(head2)


findMergeNode(head1, head2)
