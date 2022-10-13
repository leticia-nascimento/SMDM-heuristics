class Solution:
    def __init__(self, graph):
        self.graph = graph
        self.communities = []
        self.density = 0
        self.vertices_communities = {}
        for vertice in graph.vertices:
            self.vertices_communities[vertice] = None

    def add_communities(self, communities):
        for community in communities:
            self.add_community(community)

    def add_community(self, community):
        if community in self.communities:
            print("Error: Can't add ", community, "to communities.")
            return 0
        self.communities.append(community)
        # self.vertices_communities[community_index] = community_index
        for vertice_index in range(len(community)):
            self.vertices_communities[vertice_index] = self.communities.index(
                community)
