class Node:
    def __init__(self, data):
        self.prev = None
        self.next = None
        self.data = data

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            n = n.next
        n.next = new_node

    def print_list(self):
        n = self.head
        while n is not None:
            print(n.data, end="->")
            n = n.next

def combine(dllA, dllB):
    if not dllA.head:
        return dllB
    if not dllB.head:
        return dllA

    tail = dllA.head
    while tail.next:
        tail = tail.next

    tail.next = dllB.head
    dllB.head.prev = tail

    return dllA

dll1 = DoublyLinkedList()
dll1.add_end(10)
dll1.add_end(11)
dll1.add_end(12)
dll1.add_end(13)
dll1.print_list()
print()
dll2 = DoublyLinkedList()
dll2.add_end(20)
dll2.add_end(21)
dll2.add_end(22)
dll2.add_end(23)
dll2.print_list()
print()


combine(dll1, dll2).print_list()