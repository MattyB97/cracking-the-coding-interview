# 2.2 Return kth to last: Implement an algorithm to find the kth to last element in a singly linked list
# Time Complexity: O(n*n)
# Space Complexity: O(n)
from Linked_Lists.Linked_List import Node
from Linked_Lists.Linked_List import SLinkedList


def kth_to_last_pointers(list: SLinkedList, index: int) -> Node:
    if list.head is None:
        return Node(-1)
    slow = list.head
    while slow is not None:
        fast = slow
        cnt = 0
        while cnt < index and fast.next is not None:
            cnt += 1
            fast = fast.next
        if cnt == index and fast.next is None:
            return slow
        if fast.next is None:
            return Node(-1)
        else:
            slow = slow.next

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
# print()
# print(kth_to_last_pointers(list, 3).data)
