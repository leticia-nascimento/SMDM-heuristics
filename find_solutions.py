from solution import Solution
from modularity import Modularity
from copy import deepcopy
import random


class FindSolutions:
    def __init__(self, graph, LAMBDA, DEBUG):
        self.graph = graph
        self.LAMBDA = LAMBDA
        self.DEBUG = DEBUG
        self.solution = Solution(graph)
        self.modularity = Modularity(graph)

        self.new_solution = deepcopy(self.solution)
        self.temp_solution = deepcopy(self.solution)
    
    def my_shuffle(self, array):
        random.shuffle(array)
        return array

    def find(self):
        if self.DEBUG: print("(FS) START Finding solutions for all vertices")
        random_vertices = self.my_shuffle(list(self.graph.vertices))
        for vertice in random_vertices:
            # print("--------------------SOLO-------------------")
            # print("(FS) Finding new solution for vertice", vertice)
            string_vertice = str(vertice)

            # adiciona comunidade do vertice sozinho a solução
            solo_community = [vertice]
            self.solution.communities.append(solo_community)
            # atualizando a comunidade do vertice inserido solo
            solo_community_index = self.solution.communities.index(
                solo_community)
            self.solution.vertices_communities[string_vertice] = solo_community_index

            # encontra densidade comunidade solo
            solo_density = self.modularity.calculate_density_signed(
                self.solution, self.LAMBDA)

            current_best_density = solo_density
            current_best_community = solo_community_index
            # print("(FS) Current communities: ", self.solution.communities)
            # print("(FS) Current best density for: ", vertice, "is", solo_density)
            # print("(FS) Current best community for: ", vertice, "is", solo_community_index)
            # print("(FS) Current vertices communities relation: ", self.solution.vertices_communities)

            self.new_solution = deepcopy(self.solution)
            for community_index, community in enumerate(self.new_solution.communities):
                # print("--------------------GROUPING--------------yh-----")
                # print("(FS) Trying new communities for vertice", vertice, "at community", community_index)
                self.temp_solution = deepcopy(self.new_solution)

                # se só houver 1 comunidade, ainda é o primeiro passo
                if (len(self.solution.communities) < 2):
                    # print("(FS) ONLY 1 COMMUNITY YET")
                    continue

                # se for a mesma comunidade solo, ignorar
                if (community == solo_community):
                    # print("(FS) Its same solo community. Ignore")
                    continue

                # começar removendo o vertice de qualquer comunidade
                vertice_community = self.temp_solution.get_community_index(
                    vertice)
                # print("(FS) Current vertice community", vertice_community)
                if (vertice_community != None):
                    self.temp_solution.communities[vertice_community].remove(
                        vertice)
                    # print("(FS) Removing vertice from its current community to try others", self.temp_solution.communities)

                # adicionar a uma nova comunidade
                self.temp_solution.communities[community_index].append(
                    vertice)
                self.temp_solution.vertices_communities[vertice] = community_index

                # calcular nova densidade nessa comunidade
                new_density = self.modularity.calculate_density_signed(
                    self.temp_solution, self.LAMBDA)
                # print("(FS) New density with community", community_index, "Density:", new_density)
                # print("(FS) New solution communities: ",
                #   self.temp_solution.communities)

                # caso encontre uma comunidade melhor, salva os valores
                if (new_density > current_best_density):
                    # print("(FS) Best solution for", vertice, "found", self.temp_solution.communities,
                    #       "Density: ", new_density)
                    current_best_density = new_density
                    current_best_community = community_index
                    self.solution = deepcopy(self.temp_solution)
                # else:
                #     print("(FS) Previous density was better", current_best_density, "Continuing...")
            # print("--------------------")
            # print("(FS) Current communities: ", self.solution.communities)
            # print("(FS) Current best density for: ", vertice, "is", solo_density)
            # print("(FS) Current best community for: ", vertice, "is", solo_community_index)
            # print("(FS) Current vertices communities relation: ", self.solution.vertices_communities)
        # print("--------------------")
        final_density = self.modularity.calculate_density_signed(
            self.solution, self.LAMBDA)

        if self.DEBUG: print("Solution density: ", final_density)
        if self.DEBUG: print("Solution communities: ", self.solution.communities)
        return self.solution
