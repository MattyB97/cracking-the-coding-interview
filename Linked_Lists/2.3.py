# Delete Middle Node: Implement an algorithm to delete a middle node
# Note that middle node simply means not head or tail node
# Time Complexity: O(n) where n is the length of the singly linked list
# Space Complexity: O(n) where n is the length of the singly linked list
from Linked_Lists.Linked_List import Node
from Linked_Lists.Linked_List import SLinkedList


def delete_middle_node(list: SLinkedList, node: Node) -> SLinkedList:
    if list.head is node:
        list.head = list.head.next
        return list
    cur_node = list.head
    while cur_node.next is not None:
        if cur_node.next == node:
            cur_node.next = node.next
            return list
        cur_node = cur_node.next
    return

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
# list = delete_middle_node(list, list.head)
# list.list_print()
