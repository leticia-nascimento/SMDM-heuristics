class Solution:
    def __init__(self, graph):
        self.graph = graph
        self.communities = []
        self.density = float("-inf")
        self.vertices_communities = {}
        self.counted_edges = []
        for vertex in graph.vertices:
            self.vertices_communities[vertex] = None
        self.degree_node_plus = {}
        self.degree_node_minus = {}

    def get_positive_degree(self, vertex):
        if str(vertex) not in self.degree_node_plus:
            return 0
        return self.degree_node_plus[vertex]

    def get_negative_degree(self, vertex):
        if str(vertex) not in self.degree_node_minus:
            return 0
        return self.degree_node_minus[vertex]

    def get_weight(self, edge):
        vertex1 = str(edge[0])
        vertex2 = str(edge[1])
        # TODO Verificar
        # if vertice2 < vertice1:
        #     edge = (vertice2, vertice1)
        if (self.is_same_community(vertex1, vertex2)):
            if edge in self.graph.edges:
                return self.graph.get_weight(edge)
            return 0
        return 0

    # def add_vertice_to_community(self, vertice, community_index):
    #     self.vertices_communities[vertice] = community_index

    def get_community_index(self, vertice):
        for community_index, community in enumerate(self.communities):
            # print("AQUI 0 self.communities", self.communities)
            # print("AQUI 1 community_index", community_index)
            # print("AQUI 2 community", community)
            if vertice in community:
                return community_index
        return None

    def set_values(self):
        for vertice in self.graph.vertices:
            vertice_as_string = str(vertice)
            for neighbor in self.graph.neighbors[vertice]:
                weight = self.get_weight((vertice_as_string, neighbor))
                if float(weight) > 0.0:
                    self.degree_node_plus[vertice_as_string] += float(weight)
                else:
                    self.degree_node_minus[vertice_as_string] += (
                        float(weight) * -1.0)

    def get_neighbors(self, vertice):
        neighbors = []
        for neighbor in self.graph.get_neighbors(vertice):
            if self.is_same_community(vertice, neighbor):
                neighbors.append(neighbor)
        return neighbors

    def is_same_community(self, vertice1, vertice2):
        return self.vertices_communities[vertice1] == self.vertices_communities[vertice2]

    def add_communities(self, communities):
        for community in communities:
            self.add_community(community)

        self.set_values()

    def add_community(self, community):
        if community in self.communities:
            print("Error: Can't add ", community, "to communities.")
            return 0
        self.communities.append(community)
        for index in range(len(community)):
            vertice = str(community[index])
            self.vertices_communities[vertice] = self.communities.index(
                community)
            self.degree_node_plus[vertice] = 0
            self.degree_node_minus[vertice] = 0
