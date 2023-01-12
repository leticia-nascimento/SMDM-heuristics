from solution import Solution
from modularity import Modularity
from copy import deepcopy


class FindSolutions:
    def __init__(self, graph, LAMBDA):
        self.graph = graph
        self.LAMBDA = LAMBDA
        self.solution = Solution(graph)
        self.new_solution = deepcopy(self.solution)
        self.temp_solution = deepcopy(self.solution)
        self.modularity = Modularity(graph)

    def find(self):
        print("(FS) START Finding solutions for all vertices")
        self.new_solution.communities.append([])
        # aqui deve ser aleatorio. talvez só randomizar a lista de vertices
        for vertice in self.graph.vertices:
            print("(FS) Finding new solution for vertice", vertice)
            string_vertice = str(vertice)

            # # adiciona comunidade de vertice sozinho a solução
            # solo_community = [vertice]
            # self.solution.communities.append(solo_community)
            # print("(FS) Communities: ", self.solution.communities)

            # # atualizando a comunidade do vertice inserido solo
            # solo_community_index = self.solution.communities.index(
            #     solo_community)
            # print("(FS) Solo community_index: ", solo_community_index)
            # self.solution.vertices_communities[string_vertice] = solo_community_index
            # print("(FS) Solution vertices communities relation: ", self.solution.vertices_communities)
            
            # # encontra densidade comunidade solo
            # solo_density = self.modularity.calculate_density_signed(
            #     self.solution, self.LAMBDA)
            # print("(FS) Solo density for", vertice,
            #       "Density: ", solo_density)

            # print("(FS) Current communities: ", self.solution.communities)
            # print("(FS) Current best density for: ", vertice, "is", solo_density)
            current_best_density = 0
            current_best_community = None
            for community_index, community in enumerate(self.new_solution.communities):
                print("(FS) Trying new communities for vertice", vertice)
                self.temp_solution = deepcopy(self.new_solution)

                # se só houver 1 comunidade, ainda é o primeiro passo
                # if (len(self.solution.communities) < 2):
                #     print("(FS) ONLY 1 COMMUNITY YET")
                #     continue
            
                # se for a mesma comunidade solo, ignorar
                # if (community == solo_community):
                #     print("(FS) Its same solo community. Ignore")
                #     continue
                
                # começar removendo o vertice de qualquer comunidade
                vertice_community = self.temp_solution.get_community_index(vertice)
                print("(FS) Vertice community", vertice_community)
                if (vertice_community != None):
                    self.temp_solution.communities[vertice_community].remove(
                        vertice)
                    print("(FS) Removing vertice from its community to try others", self.temp_solution.communities)

                # adicionar a uma nova comunidade
                self.temp_solution.communities[community_index].append(
                    vertice)
                new_density = self.modularity.calculate_density_signed(
                    self.temp_solution, self.LAMBDA)
                print("(FS) Trying new solution for", vertice, "at community", community_index,
                      "Density: ", new_density)
                print("(FS) New solution communities: ",
                      self.temp_solution.communities)
                self.temp_solution.vertices_communities[vertice] = community_index

                if (self.temp_solution.density > current_best_density):
                    print("(FS) Best solution for", vertice, "found", self.temp_solution.communities,
                          "Density: ", self.solution.density)
                    current_best_density = new_density
                    current_best_community = community_index
                # else:
                #     self.solution.communities[community_index].remove(
                #     vertice)
                #     new_solo_community = [vertice]
                #     self.solution.communities.append(new_solo_community)
                #     self.solution.vertices_communities[string_vertice] = community_index
                #     print("(FS) Solo solution was best for", vertice,
                #           "Density: ", self.solution.density)
            self.new_solution = deepcopy(self.temp_solution)
        return self.solution.communities
