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
        self.neighbours = {}
        self.weights = {}
        self.degrees = {}

    def add_vertice(self, vertice_index, vertice_name):
        if self.vertice_exists(vertice_index):
            print("Error: Can't add ", vertice_index, "to vertices.")
            return 0
        self.vertices.add(vertice_index)
        self.vertices_names[vertice_index] = vertice_name
        self.degrees[vertice_index] = 0
        self.neighbours[vertice_index] = set()

    def add_edges(self, edge, weight):
        if not self.is_edge_valid(edge):
            print("Error: Can't add ", edge, "to edges.")
            return 0
        self.edges.append(edge)
        self.weights[edge] = float(weight)
        for index, vertice in enumerate(edge):
            neighbour = edge[(index + 1) % 2]
            self.neighbours[vertice].add(neighbour)
            self.degrees[vertice] += 1

    def is_edge_valid(self, edge):
        if len(edge) != 2:
            return False

        for e in edge:
            if e not in self.vertices:
                return False

        if edge in self.edges:
            return False
        return True

    def vertice_exists(self, vertice):
        return vertice in self.vertices

    def num_vertices(self):
        return len(self.vertices)

    def num_edges(self):
        return len(self.edges)

    def get_degree(self, vertice):
        if not self.vertice_exists(vertice):
            print("Error: ", vertice, "doesn't exist.")
            return 0
        return self.degrees[vertice]

    def get_weight(self, edge):
        if edge in self.edges:
            return self.weights[edge]
        return float('inf')

    def get_neighbours(self, vertice):
        return self.neighbours[vertice]

    def read_file(self, file_name):
        import re
        file = open(file_name, 'r')
        content = file.readlines()
        file.close()

        vertices_step = False
        edges_step = False

        vertice_re = re.compile("^(\d+)\s(.+)$")  # ex. 1 name
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
                vertice = vertice_re.search(string)
                vertice_index = vertice.group(1)
                vertice_name = vertice.group(2)
                self.add_vertice(vertice_index, vertice_name)
            if edges_step:
                edge = edge_re.findall(string)
                # ex: edge[0] = vertice 1, edge[1] = vertice 2, edge[2] = weigth
                self.add_edges((edge[0], edge[1]), edge[2])
