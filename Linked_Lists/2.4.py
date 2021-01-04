# Partition: Write code to partition a linked list around a value x. Any node with a data value less than or equal
# to 'x' should appear on the left side and any value greater than 'x' should appear on the right side.
# CURRENTLY NOT RUNNING.
# CONFIRMED SOL WITH BACK OF BOOK BUT I THINK THERE IS AN ISSUE WITH THE UNDERLYING DATA STRUCTURE
# Space Complexity: O(n) where n is the size of the list
# Time Complexity: O(n) where n is the size of the list
from Linked_Lists.Linked_List import Node
from Linked_Lists.Linked_List import SLinkedList

def partition(list: SLinkedList, val: int) -> SLinkedList:
    head = list.head
    tail = list.head
    cur_node = list.head
    while cur_node is not None:
        cur_node.next = None
        if cur_node.data < val:
            cur_node.next = head
            head = cur_node
        else:
            tail.next = cur_node
            tail = cur_node
        cur_node = cur_node.next
    tail.next = None
    return head





# Driver Code
list = SLinkedList()
list.head = Node(1)
n1 = Node(1)
n2 = Node(3)
n3 = Node(4)
n4 = Node(3)
list.head.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
print()
list = partition(list, 4)
list.list_print()