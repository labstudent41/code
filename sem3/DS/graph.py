class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)

    def delete_vertex(self, vertex):
        if vertex in self.graph:
            del self.graph[vertex]
            for other_vertex in self.graph:
                self.graph[other_vertex] = [v for v in self.graph[other_vertex] if v != vertex]

    def __str__(self):
        graph = ""
        for key in self.graph.keys():
            graph += key + ' -> ' + str(self.graph[key]) + '\n'
        return graph

# Create a graph
graph = Graph()

# Add vertices
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")

# Add edges
graph.add_edge("A", "B")
graph.add_edge("B", "C")
graph.add_edge("C", "D")
graph.add_edge("D", "A")

print("Graph after adding vertices and edges:")
print(graph)

# Delete a vertex
vertex_to_delete = "B"
graph.delete_vertex(vertex_to_delete)

print("Graph after deleting vertex", vertex_to_delete)
print(graph)
