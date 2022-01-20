from queue import Queue

class Vertex:
    def __init__(self, name):
        self.name = name
        self.adjacent_vertices = []

    def add_adjacent_vertex(self, vertex):
        if vertex in self.adjacent_vertices:
            return
        self.adjacent_vertices.append(vertex)
        vertex.add_adjacent_vertex(self)


idris = Vertex("Idris")
kamil = Vertex("Kamil")
talia = Vertex("Talia")
lina = Vertex("Lina")
ken = Vertex("Ken")
marco = Vertex("Marco")
sasha = Vertex("Sasha")
bob = Vertex("bob")

idris.add_adjacent_vertex(kamil)
idris.add_adjacent_vertex(talia)
kamil.add_adjacent_vertex(lina)
talia.add_adjacent_vertex(ken)
lina.add_adjacent_vertex(sasha)
#lina.add_adjacent_vertex(marco)
ken.add_adjacent_vertex(marco)
marco.add_adjacent_vertex(sasha)
sasha.add_adjacent_vertex(bob)

def shortest_path1(starting_vertex, search_vertex, visited_vertices = {}):
    queue = Queue(0)
    shortest_number_person_table = {}
    shortest_previous_person_table = {}

    queue.put(starting_vertex)

    shortest_number_person_table[starting_vertex.name] = 0
    while not queue.empty():
        current_vertex = queue.get()
        visited_vertices[current_vertex.name] = True

        for adjacent_vertex in current_vertex.adjacent_vertices:
            if visited_vertices.get(adjacent_vertex.name):
                continue

            visited_vertices[adjacent_vertex.name] = True
            queue.put(adjacent_vertex)
            number_to_adjacent_vertex_from_starting = shortest_number_person_table[current_vertex.name] + 1
            if not shortest_number_person_table.get(adjacent_vertex.name) or \
                    number_to_adjacent_vertex_from_starting < shortest_number_person_table.get(adjacent_vertex.name):
                shortest_number_person_table[adjacent_vertex.name] = number_to_adjacent_vertex_from_starting
                shortest_previous_person_table[adjacent_vertex.name] = current_vertex.name
            if adjacent_vertex.name == search_vertex.name:
                path = []
                print([shortest_number_person_table, shortest_previous_person_table])
                current_vertex = search_vertex.name
                while current_vertex != starting_vertex.name:
                    path.append(current_vertex)
                    current_vertex = shortest_previous_person_table[current_vertex]
                path.append(starting_vertex.name)
                path.reverse()
                return path



    return None


def shortest_path2(first_vertex, second_vertex, visited_vertices = {}):
    queue = Queue(0)

    previous_vertex_table = {}
    visited_vertices[first_vertex.name] = True
    queue.put(first_vertex)

    while not queue.empty():
        current_vertex = queue.get()
        for adjacent_vertex in current_vertex.adjacent_vertices:
            if not visited_vertices.get(adjacent_vertex.name):
                visited_vertices[adjacent_vertex.name] = True
                queue.put(adjacent_vertex)
                previous_vertex_table[adjacent_vertex.name] = current_vertex.name

    shortest_path = []
    current_vertex_value = second_vertex.name

    while current_vertex_value != first_vertex.name:
        shortest_path.append(current_vertex_value)
        current_vertex_value = previous_vertex_table[current_vertex_value]

    shortest_path.append(first_vertex.name)
    shortest_path.reverse()

    return shortest_path






print(shortest_path1(idris, marco))
print(shortest_path2(idris, marco))























