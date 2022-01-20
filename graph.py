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

def dfs(vertex, search_value, visited_vertices={}):
    if vertex.value == search_value:
        return vertex

    visited_vertices[vertex.value] = True

    for adjacent_vertex in vertex.adjacent_vertices:
        if visited_vertices.get(adjacent_vertex.value):
            continue

        if adjacent_vertex.value == search_value:
            return adjacent_vertex

        vertex_to_search = dfs(adjacent_vertex, search_value, visited_vertices)

        if vertex_to_search:
            return vertex_to_search

    return None



def bfs_traverse(starting_vertex):
    queue = Queue(0)

    visited_vertices = {}
    visited_vertices[starting_vertex.value] = True
    queue.put(starting_vertex)

    while not queue.empty():
        current_vertex = queue.get()
        print(current_vertex.value)

        for adjacent_vertex in current_vertex.adjacent_vertices:
            if visited_vertices.get(adjacent_vertex.value):
                continue
            else:
                visited_vertices[adjacent_vertex.value] = True
                queue.put(adjacent_vertex)


def bfs(starting_index, search_value):
    queue = Queue(0)
    visited_vertices = {}
    visited_vertices[starting_index.value] = True
    queue.put(starting_index)

    while not queue.empty():
        current_vertex = queue.get()
        if current_vertex.value == search_value:
            return current_vertex

        for adjacent_vertex in current_vertex.adjacent_vertices:
            if not visited_vertices.get(adjacent_vertex.value):
                visited_vertices[adjacent_vertex.value] = True
                queue.put(adjacent_vertex)











alice = Vertex("alice")
bob = Vertex("bob")
cynthia = Vertex("cynthia")

alice.add_adjacent_vertex(bob)
alice.add_adjacent_vertex(cynthia)
bob.add_adjacent_vertex(cynthia)



dfs_traverse(bob)


bfs_traverse(alice)

print(bfs(alice, "cynthi"))