class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class SLinkedList:
    def __init__(self):
        self.head = None

    def list_print(self):
        cur_node = self.head
        while cur_node is not None:
            print(cur_node.data)
            cur_node = cur_node.next

    def append_to_tail(self, node: Node):
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = node

    def append_to_head(self, node: Node):
        temp = self.head
        self.head = node
        node.next = temp

    def append_at(self, node: Node, val: int):
        if val == 0:
            self.append_to_head(node)
            return
        cur_node = self.head
        for i in range(val - 1):
            if cur_node.next is None:
                break
            cur_node = cur_node.next
        node.next, cur_node.next = cur_node.next, node

    def remove_head(self):
        self.head = self.head.next

    def remove_at(self, val: int):
        if val == 0:
            self.remove_head()
        cur_node = self.head
        for i in range(val - 1):
            if cur_node.next.next is None:
                break
            cur_node = cur_node.next
        cur_node.next = cur_node.next.next


class DLinkedList:
    def __init__(self):
        self.head = None

    def list_print(self):
        cur_node = self.head
        while cur_node is not None:
            print(f"{cur_node.data}, Prev: {cur_node.prev.data if cur_node.prev else 'NONE'}")
            cur_node = cur_node.next

    def append_to_tail(self, node: Node):
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
        cur_node.next = node
        node.prev = cur_node
        node.next = None

    def append_to_head(self, node: Node):
        self.head, node.next = node, self.head
        node.next.prev = node

    def append_at(self, node: Node, val: int):
        if val == 0:
            self.append_to_head(node)
            return
        cur_node = self.head
        for i in range(val - 1):
            if cur_node.next is None:
                cur_node.next = node
                node.prev = cur_node
                node.next = None
                return
            cur_node = cur_node.next
        node.prev, node.next, cur_node.next, cur_node.next.next.prev = cur_node, cur_node.next, node, node

    def remove_tail(self):
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
        cur_node.prev.next = cur_node.next
        cur_node.prev = None

    def remove_head(self):
        self.head = self.head.next
        self.head.prev = None

    def remove_at(self, val: int):
        if val == 0:
            self.remove_head()
        cur_node = self.head
        for i in range(val):
            if cur_node.next is None:
                cur_node.prev.next = cur_node.next
                cur_node.prev = None
                return
            cur_node = cur_node.next

        cur_node.next = cur_node.next.next
        cur_node.next.prev = cur_node


# # Driver Code
# linked_list = DLinkedList()
# linked_list.head = Node("Mon")
# e2 = Node("Tue")
# e3 = Node("Wed")
# e4 = Node("Thu")
# e5 = Node("Sun")
# e6 = Node("Fri")
# e7 = Node("Sat")
# linked_list.head.next = e2
# e2.prev = linked_list.head
# e2.next = e3
# e3.prev = e2
# e3.next = e4
# e4.prev = e3
# e4.next = None
#
# linked_list.list_print()
# linked_list.append_to_head(e5)
# linked_list.append_to_tail(e6)
# linked_list.append_at(e7, 7)
# print()
# linked_list.list_print()
# print()
# linked_list.remove_tail()
# linked_list.remove_head()
# linked_list.list_print()
# print()
# linked_list.remove_at(1)
# linked_list.list_print()
#
# # linked_list.head.next = e2
# # e2.next = e3
# #
# # linked_list.list_print()
# #
# # linked_list.append_to_tail(e4)
# # linked_list.append_to_head(e5)
# # linked_list.list_print()
# # print('')
# # linked_list.append_at(e6, 9)
# # linked_list.remove_at(0)
# # linked_list.list_print()
