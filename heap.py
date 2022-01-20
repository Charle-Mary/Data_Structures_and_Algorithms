class Heap:
    def __init__(self):
        self.data = []

    myhap = 6
    def rootnode(self):
        return self.data.first

    def lastnode(self):
        return self.data.last

    def left_child_index(self, index):
        return (index * 2) + 1

    def right_child_index(self, index):
        return (index * 2) + 2

    def parent_index(self, index):
        return (index - 1) // 2

    def insertmax(self, value):
        self.data.append(value)

        new_node_index = len(self.data) - 1

        while new_node_index > 0 and \
                self.data[new_node_index] > self.data[self.parent_index(new_node_index)]:
            self.data[new_node_index], self.data[self.parent_index(new_node_index)] \
                = self.data[self.parent_index(new_node_index)], self.data[new_node_index]

            new_node_index = self.parent_index(new_node_index)

    def insertmin(self, value):
        self.data.append(value)

        new_node_index = len(self.data) - 1

        while new_node_index > 0 and \
            self.data[new_node_index] < self.data[self.parent_index(new_node_index)]:
            self.data[new_node_index], self.data[self.parent_index(new_node_index)] \
            = self.data[self.parent_index(new_node_index)], self.data[new_node_index]

            new_node_index = self.parent_index(new_node_index)



    def has_greater_child(self, index):
        try:
            return (self.data[self.left_child_index(index)] and self.data[self.left_child_index(index)] > self.data[index]) or \
            (self.data[self.right_child_index(index)] and self.data[self.right_child_index(index)] > self.data[index])
        except IndexError:
            return False


    def calculate_larger_child(self, index):
        try:
            if self.data[self.left_child_index(index)] > self.data[self.right_child_index(index)]:
                return self.left_child_index(index)
        except IndexError:
            return self.left_child_index(index)

        try:
            if self.data[self.right_child_index(index)] > self.data[self.left_child_index(index)]:
                return self.right_child_index(index)
        except IndexError:
            return self.right_child_index(index)

    def has_lesser_child(self, index):
        try:
            return (self.data[self.left_child_index(index)] and self.data[self.left_child_index(index)] < self.data[index]) or \
                    (self.data[self.right_child_index(index)] and self.data[self.right_child_index(index)] < self.data[index])
        except IndexError:
            return False

    def less_child_index(self, index):
        try:
            if self.data[self.left_child_index(index)] < self.data[self.right_child_index(index)]:
                return self.left_child_index(index)
        except IndexError:
            return self.left_child_index(index)

        try:
            if self.data[self.right_child_index(index)] < self.data[self.left_child_index(index)]:
                return self.right_child_index(index)
        except IndexError:
            return self.right_child_index(index)



    def deletedes(self):
        try:
            self.data[0] = self.data.pop()
        except IndexError:
            return

        trickle_node_index = 0


        while self.has_greater_child(trickle_node_index):
            larger_child_index = self.calculate_larger_child(trickle_node_index)

            self.data[trickle_node_index], self.data[larger_child_index] = \
            self.data[larger_child_index], self.data[trickle_node_index]

            trickle_node_index = larger_child_index


    def deleteas(self):
        try:
            self.data[0] = self.data.pop()
        except IndexError:
            return

        trickle_node = 0

        while self.has_lesser_child(trickle_node):
            lesser_child_index = self.less_child_index(trickle_node)

            self.data[trickle_node], self.data[lesser_child_index] = \
            self.data[lesser_child_index], self.data[trickle_node]

            trickle_node = lesser_child_index




    def values(self):
        return [self.data, self.myhap]

    def sortdes(self):
        newarr = []

        while len(self.data) > 0:
            newarr.append(self.data[0])
            self.deletedes()

        return newarr

    def sortas(self):
        newarr = []

        while len(self.data) > 0:
            newarr.append(self.data[0])
            self.deleteas()

        return newarr



myheap = Heap()

myheap.insertmax(-7)
myheap.insertmax(-4)
myheap.insertmax(-8)
myheap.insertmax(2)
myheap.insertmax(-6)
# myheap.insertmax(10)
# myheap.insertmax(2)
# myheap.insertmax(99)
# myheap.insertmax(68)


print(myheap.values())

# print(myheap.sortas())