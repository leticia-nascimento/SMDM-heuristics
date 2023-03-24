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

    def add_vertice(self, vertice, vertice_name):
        if self.vertice_exists(vertice):
            print("Error: Can't add ", vertice, "to vertices.")
            return 0
        self.vertices.add(vertice)
        self.vertices_names[vertice] = vertice_name
        self.degrees[vertice] = 0
        self.degree_node_plus[vertice] = 0
        self.degree_node_minus[vertice] = 0
        self.neighbors[vertice] = set()

    def add_edges(self, edge, weight):
        if not self.is_edge_valid(edge):
            print("Error: Can't add ", edge, "to edges.")
            return 0
        self.edges.append(edge)
        self.weights[edge] = float(weight)
        for index, vertice in enumerate(edge):
            neighbors = edge[(index + 1) % 2]
            self.neighbors[vertice].add(neighbors)
            self.degrees[vertice] += 1
            if float(weight) > 0.0:
                self.degree_node_plus[vertice] += float(weight)
            else:
                self.degree_node_minus[vertice] += (float(weight) * -1.0)

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

    # def get_edge(self, vertice_a, vertice_b):
    #     for edge in self.edges:
    #         if [vertice_a, vertice_b] == edge:
    #             return edge
    #     return None

    # def get_adj(self, vertice_a, vertice_b):
    #     if vertice_b not in self.neighbors[vertice_a]:
    #         return 0
    #     edge = self.get_edge(vertice_a, vertice_b)
    #     return self.get_weight[edge]

    def get_positive_degree(self, vertice):
        if vertice not in self.degree_node_plus:
            return 0
        return self.degree_node_plus[vertice]

    def get_negative_degree(self, vertice):
        if vertice not in self.degree_node_minus:
            return 0
        return self.degree_node_minus[vertice]

    def get_degree(self, vertice):
        if not self.vertice_exists(vertice):
            print("Error: ", vertice, "doesn't exist.")
            return 0
        return self.degrees[vertice]

    def get_weight(self, edge):
        if edge in self.edges:
            return self.weights[edge]
        return 0

    def get_neighbors(self, vertice):
        return self.neighbors[vertice]

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
