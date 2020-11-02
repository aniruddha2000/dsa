from singlyLinkedList import LinkedList


a = LinkedList(5)
head1 = a.create_linked_list()


def has_cycle(head):
    if head is None:
        return 0
    slow = head
    fast = head.next
    while fast != None and fast.next != None:
        if slow == fast:
            return 1
        slow = slow.next
        fast = fast.next.next
    return 0


print(has_cycle(head1))
