class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.first_node = None

    def read(self, index):
        current_node = self.first_node
        current_index = 0

        while current_index < index:
            if current_node.next == None:
                return
            current_node = current_node.next
            current_index += 1

        return current_node.data

    def index_of(self, value):
        current_node = self.first_node
        current_index = 0

        while current_node:
            if current_node.data == value:
                return current_index

            else:
                current_node = current_node.next
                current_index += 1

        return None

    def insert_in(self, index, value):
        node = Node(value)

        if index == 0:
            node.next = self.first_node
            self.first_node = node
            return

        current_node = self.first_node
        current_index = 0

        while current_index < index - 1:
            current_node = current_node.next
            current_index += 1

            if current_node == None:
                return

        node.next = current_node.next
        current_node.next = node

        return

    def delete_at_index(self, index):
        current_node = self.first_node
        current_index = 0
        if index == 0:
            self.first_node = current_node.next

        while current_index < index - 1:
            current_node = current_node.next
            current_index += 1

            if current_node.next == None:
                return

        current_node.next = current_node.next.next

        return

    def traverse(self, node):
        if node is not None:
            print(node.data, end=' ')
            self.traverse(node.next)




node1 = Node(5)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.next = node2
node2.next = node3
node3.next = node4

_list = LinkedList()
_list.first_node = node1

_list.traverse(node1)

# print(_list.read(3))
#
# print(_list.index_of(100))
#
# _list.insert_in(4, 100)
#
# print(_list.read(4))
#
# _list.delete_at_index(4)
#
# print(_list.read(4))


