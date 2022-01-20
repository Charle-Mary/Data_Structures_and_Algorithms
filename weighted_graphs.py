class City:
    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = {}

    def add_adjacent_vertex(self, vertex, weight):
        self.adjacent_vertices[vertex] = weight


dallas = City("dallas")
toronto = City("toronto")

dallas.add_adjacent_vertex(toronto, 138)
toronto.add_adjacent_vertex(dallas, 216)

