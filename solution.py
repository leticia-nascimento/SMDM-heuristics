class Solution:
    def __init__(self, graph):
        self.graph = graph
        self.communities = []
        self.density = 0
        self.vertices_communities = {}
        # self.edges_communities = {}
        self.counted_edges = []
        for vertice in graph.vertices:
            self.vertices_communities[vertice] = None
        # for edges in graph.edges:
        #     self.edges_communities = None
        # self.weights = {}
        self.degree_node_plus = {}
        self.degree_node_minus = {}

    # def set_edges(self):
    #     for edge in self.graph.edges:
    #         vertice1 = str(edge[0])
    #         vertice2 = str(edge[1])
    #         if (self.is_same_community(vertice1, vertice2)):
    #             self.add_edges(self.vertices_communities[vertice1], edge)

    def get_positive_degree(self, vertice):
        if str(vertice) not in self.degree_node_plus:
            return 0
        return self.degree_node_plus[vertice]

    def get_negative_degree(self, vertice):
        # print("vertice", str(vertice))
        # print("self.degree_node_minus", self.degree_node_minus)
        if str(vertice) not in self.degree_node_minus:
            return 0
        return self.degree_node_minus[vertice]

    def get_weight(self, edge):
        vertice1 = str(edge[0])
        vertice2 = str(edge[1])
        # if edge in self.counted_edges:
        #     return 0
        if vertice2 < vertice1:
            edge = (vertice2, vertice1)
        # if edge in self.counted_edges:
        #     return 0
        if (self.is_same_community(vertice1, vertice2)):
            if edge in self.graph.edges:
                return self.graph.get_weight(edge)
            return 0
        return 0

    def set_values(self):
        for vertice in self.graph.vertices:
            vertice_as_string = str(vertice)
            for neighbour in self.graph.neighbours[vertice]:
                weight = self.get_weight((vertice_as_string, neighbour))
                if float(weight) > 0.0:
                    self.degree_node_plus[vertice_as_string] += float(weight)
                else:
                    self.degree_node_minus[vertice_as_string] += (float(weight) * -1.0)

    def is_same_community(self, vertice1, vertice2):
        return self.vertices_communities[vertice1] == self.vertices_communities[vertice2]

    def add_communities(self, communities):
        for community in communities:
            self.add_community(community)

        # self.set_edges()
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

    # def add_edges(self, community_index, edge):
    #     index = str(community_index)
    #     print("self.edges_communities",
    #           self.edges_communities)
    #     self.edges_communities[edge] = index
        # self.weights[edge] = float(weight)
        # for index, vertice in enumerate(edge):
        #     neighbour = edge[(index + 1) % 2]
        # self.neighbours[vertice].add(neighbour)
        # self.degrees[vertice] += 1
        # if float(weight) > 0.0:
        #     self.degree_node_plus[vertice] += float(weight)
        # else:
        #     self.degree_node_minus[vertice] += (float(weight) * -1.0)
