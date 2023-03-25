class Graph:
    '''
    Base class for undirected and weighted graph G(V, E, w), where:
        V represents a set of vertices;
        E represents a list of edges;
        w represents a list of weights.
    '''

    def __init__(self, id):
        self.id = id
        self.vertices = set()
        self.vertices_names = {}
        self.edges = []
        self.neighbors = {}
        self.weights = {}
        self.degrees = {}
        self.degree_node_plus = {}
        self.degree_node_minus = {}

    def add_vertex(self, vertex, vertex_name):
        if self.vertex_exists(vertex):
            print("Error: Can't add ", vertex, "to vertices.")
            return 0
        self.vertices.add(vertex)
        self.vertices_names[vertex] = vertex_name
        self.degrees[vertex] = 0
        self.degree_node_plus[vertex] = 0
        self.degree_node_minus[vertex] = 0
        self.neighbors[vertex] = set()

    def add_edges(self, edge, weight):
        if not self.is_edge_valid(edge):
            print("Error: Can't add ", edge, "to edges.")
            return 0
        self.edges.append(edge)
        self.weights[edge] = float(weight)
        for index, vertex in enumerate(edge):
            neighbors = edge[(index + 1) % 2]
            self.neighbors[vertex].add(neighbors)
            self.degrees[vertex] += 1
            if float(weight) > 0.0:
                self.degree_node_plus[vertex] += float(weight)
            else:
                self.degree_node_minus[vertex] += (float(weight) * -1.0)

    def is_edge_valid(self, edge):
        if len(edge) != 2:
            return False

        for e in edge:
            if e not in self.vertices:
                return False

        if edge in self.edges:
            return False
        return True

    def vertex_exists(self, vertex):
        return vertex in self.vertices

    def num_vertices(self):
        return len(self.vertices)

    def num_edges(self):
        return len(self.edges)

    # def get_edge(self, vertex_a, vertex_b):
    #     for edge in self.edges:
    #         if [vertex_a, vertex_b] == edge:
    #             return edge
    #     return None

    # def get_adj(self, vertex_a, vertex_b):
    #     if vertex_b not in self.neighbors[vertex_a]:
    #         return 0
    #     edge = self.get_edge(vertex_a, vertex_b)
    #     return self.get_weight[edge]

    def get_positive_degree(self, vertex):
        if vertex not in self.degree_node_plus:
            return 0
        return self.degree_node_plus[vertex]

    def get_negative_degree(self, vertex):
        if vertex not in self.degree_node_minus:
            return 0
        return self.degree_node_minus[vertex]

    def get_degree(self, vertex):
        if not self.vertex_exists(vertex):
            print("Error: ", vertex, "doesn't exist.")
            return 0
        return self.degrees[vertex]

    def get_weight(self, edge):
        if edge in self.edges:
            return self.weights[edge]
        return 0

    def get_neighbors(self, vertex):
        return self.neighbors[vertex]

    def read_file(self, file_name):
        import re
        file = open(file_name, 'r')
        content = file.readlines()
        file.close()

        vertices_step = False
        edges_step = False

        vertex_re = re.compile("^(\d+)\s(.+)$")  # ex. 1 name
        edge_re = re.compile('([^\s]+)')  # ex. 1 2 1

        for string in content:
            if "*vertices" in string:
                vertices_step = True
                continue
            if "*edges" in string:
                vertices_step = False
                edges_step = True
                continue
            if vertices_step:
                vertex = vertex_re.search(string)
                vertex_index = vertex.group(1)
                vertex_name = vertex.group(2)
                self.add_vertex(vertex_index, vertex_name)
            if edges_step:
                edge = edge_re.findall(string)
                # ex: edge[0] = vertex 1, edge[1] = vertex 2, edge[2] = weight
                self.add_edges((edge[0], edge[1]), edge[2])
