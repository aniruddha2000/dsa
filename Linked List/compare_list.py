from singlyLinkedList import LinkedList


a = LinkedList(5)
head1 = a.create_linked_list()
b = LinkedList(5)
head2 = b.create_linked_list()

def compare_list(head1, head2):
    while head1 != None and head2 != None:
        if head1.data != head2.data:
            return False
        head1 = head1.next
        head2 = head2.next
    return (head1 == None and head2 == None)

print(compare_list(head1, head2))
