class Node:
    def __init__(self, node):
        self.node = node
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        self.firstnode = None
        self.lastnode = None

    def delete_first(self):
        self.firstnode = self.firstnode.next



    def insert_at_end(self, value):
        node = Node(value)
        if not self.firstnode:
            self.firstnode = node
            self.lastnode = node

        else:
            node.previous = self.lastnode
            self.lastnode.next = node
            self.lastnode = node

        return


class Queue:
    def __init__(self):
        self.data = DoublyLinkedList()

    def enqueue(self, element):
        self.data.insert_at_end(element)
        return

    def dequeue(self):
        self.data.delete_first()
        return




_list = DoublyLinkedList()
node1 = Node(8)
node2 = Node(10)
node1.next = node2
node2.previous = node1

_list.firstnode = node1
_list.lastnode = node2
_list.insert_at_end(900)

print(_list.firstnode.node)

_list.delete_first()
#
print(_list.firstnode.node)

_queue = Queue

_queue.enqueue(12)
_queue.enqueue(14)

print()
