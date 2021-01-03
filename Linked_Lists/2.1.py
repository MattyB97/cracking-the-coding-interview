# 2.1 Remove Duplicates: Write code to remove duplicates from an unsorted linked list.
# Extra Challenge : Solve this problem without a temporary buffer
# Time Complexity: O(n*n) where n is the length of the linked list
# Space Complexity: O(n) where n is the length of the linked list

from Linked_Lists.Linked_List import Node
from Linked_Lists.Linked_List import SLinkedList


def remove_duplicates(list: SLinkedList) -> SLinkedList:
    slow_pointer = list.head
    while slow_pointer.next is not None:
        fast_pointer = slow_pointer
        while fast_pointer.next is not None:
            if slow_pointer.data == fast_pointer.next.data:
                fast_pointer.next = fast_pointer.next.next if fast_pointer.next.next is not None else None
            if fast_pointer.next is None:
                break
            fast_pointer = fast_pointer.next
        if slow_pointer.next is None:
            break
        slow_pointer = slow_pointer.next
    return list

# Driver Code
# list = SLinkedList()
# list.head = Node(1)
# n1 = Node(1)
# n2 = Node(3)
# n3 = Node(4)
# n4 = Node(3)
# list.head.next = n1
# n1.next = n2
# n2.next = n3
# n3.next = n4
# list.list_print()
# list = remove_duplicates(list)
# print()
# list.list_print()
