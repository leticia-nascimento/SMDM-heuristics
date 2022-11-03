from solution import Solution
from modularity import Modularity
from copy import deepcopy

# Obter a solução ótima local S'
# fazer um shuffle dos vertices e cortar pra fazer uma solução aleatoria


class LocalSearch:
    def __init__(self, graph, solution, LAMBDA):
        self.graph = graph
        self.LAMBDA = LAMBDA
        self.solution = solution
        self.new_solution = deepcopy(solution)  # conjunto de comunidades
        self.modularity = Modularity(graph)

    # Primeiramente criando soluções locais pra comparar com S
    def search(self):
        # s = [[1, 2, 3], [4, 5], [6]]
        # s1 = [[1, 2, 3, 4], [5], [6]]
        # s2 = [[1, 2, 3, 5], [4], [6]]
        # s4 = [[1, 2, 3, 6], [4, 5]]

        # s = [[2, 3], [1, 4, 5], [6]]
        # s1 = [[2, 3, 4], [4, 5], [1, 6]]
        # s2 = [[1, 2, 3, 5], [4], [6]]
        # s4 = [[1, 2, 3, 6], [4, 5]]
        print("(LS) START New solution communities: ",
              self.new_solution.communities)
        for community_index, community in enumerate(self.solution.communities):
            for vertice_index in range(len(community)):
                self.new_solution = deepcopy(self.solution)
                print("(LS) New solution communities:",
                      self.new_solution.communities)
                # pegar os vertices das comunidades e criar novas
                vertice = community[vertice_index]
                stringVertice = str(vertice)
                for next_community in range(community_index + 1, len(self.solution.communities)):
                    self.new_solution.communities[next_community].append(
                        vertice)
                    self.new_solution.vertices_communities[stringVertice] = next_community
                    self.new_solution.communities[next_community - 1].remove(
                        vertice)
                    print("(LS) New solution vertice communities:",
                          self.new_solution.vertices_communities)
                    print("(LS) New solution communities:",
                          self.new_solution.communities)
                    # if self.new_solution.communities[community_index] == []:
                    #     self.new_solution.communities.remove(community)
                    # print(" new_solution.communities 4",
                    #   self.new_solution.communities)
                    density = self.modularity.calculate_density_signed(
                        self.new_solution, self.LAMBDA)
                    print("(LS) New density", density)
                    if (self.solution.density < density):
                        print("(LS) Best solution found", self.new_solution.communities,
                              "Density: ", self.new_solution.density)
                        return density
        print("(LS) Already has the best solution", self.solution.density)
        return 0
