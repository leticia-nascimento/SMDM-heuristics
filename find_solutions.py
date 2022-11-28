from solution import Solution
from modularity import Modularity
from copy import deepcopy


class FindSolutions:
    def __init__(self, graph, LAMBDA):
        self.graph = graph
        self.LAMBDA = LAMBDA
        self.solution = Solution(graph)
        self.modularity = Modularity(graph)

    def find(self):
        print("(FS) START Finding solutions for all vertices")
        # self.solution.communities.append([])
        new_communities = []
        for vertice in self.graph.vertices:
            string_vertice = str(vertice)
            solo_community = [vertice]
            print("(FS) Finding new solution for vertice", vertice)
            self.solution.communities.append(solo_community)
            print("(FS) Communities: ", self.solution.communities)
            community_index = self.solution.communities.index(
                solo_community)
            print("(FS) Community_index: ", community_index)
            self.solution.vertices_communities[string_vertice] = community_index
            solo_density = self.modularity.calculate_density_signed(
                self.solution, self.LAMBDA)
            print("(FS) First best solution for", vertice,
                  "Density: ", solo_density)
            new_communities = self.solution.communities  # ver se copia ou se sobrepoe
            print("(FS) New communities: ", new_communities)
            for community_index, community in enumerate(new_communities):
                # começar removendo o vertice de qualquer comunidade
                vertice_community = self.solution.get_community_index(vertice)
                print("(FS) Vertice community", vertice_community)
                if (vertice_community):
                    self.solution.communities[vertice_community].remove(
                        vertice)
                # adicionar a uma nova comunidade
                self.solution.communities[community_index].append(
                    vertice)
                new_density = self.modularity.calculate_density_signed(
                    self.solution, self.LAMBDA)
                print("(FS) New solution for vertice", vertice,
                      "Density: ", new_density)
                print("(FS) New solution communities: ",
                      self.solution.communities)
                self.solution.vertices_communities[vertice] = community_index
                if (self.solution.density < solo_density):
                    print("(FS) Best solution for", vertice, "found", self.solution.communities,
                          "Density: ", self.solution.density)
            # return density
        # print("(FS) Already has the best solution", self.solution.density)
        return 0
