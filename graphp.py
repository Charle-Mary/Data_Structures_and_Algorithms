from queue import Queue

class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = []

    def add_adjacent_vertex(self, vertex):
        if vertex in self.adjacent_vertices:
            return
        self.adjacent_vertices.append(vertex)
        vertex.add_adjacent_vertex(self)


def dfs_traverse(vertex, visited_vertices = {}):
    visited_vertices[vertex.value] = True

    print(vertex.value)
    for adjacent_vertex in vertex.adjacent_vertices:
        if visited_vertices.get(adjacent_vertex.value):
            continue
        dfs_traverse(adjacent_vertex, visited_vertices)



def bfs_traverse(vertex):
    queue = Queue(0)
    visited_vertices = {}
    visited_vertices[vertex.value] = True

    queue.put(vertex)

    while not queue.empty():
        current_vertex = queue.get()
        print(current_vertex.value)

        for adjacent_vertex in current_vertex.adjacent_vertices:
            if visited_vertices.get(adjacent_vertex.value):
                continue
            visited_vertices[adjacent_vertex.value] = True
            queue.put(adjacent_vertex)




alice = Vertex("alice")
bob = Vertex("bob")
cynthia = Vertex("cynthia")

alice.add_adjacent_vertex(bob)
alice.add_adjacent_vertex(cynthia)
bob.add_adjacent_vertex(cynthia)


dfs_traverse(bob)
bfs_traverse(cynthia)
