from solution import Solution
from modularity import Modularity
from copy import deepcopy
import random


class FindSolutions:
    def __init__(self, graph, LAMBDA, VERBOSE, DEBUG_FIND_SOLUTIONS):
        self.graph = graph
        self.LAMBDA = LAMBDA
        self.VERBOSE = VERBOSE
        self.DEBUG = DEBUG_FIND_SOLUTIONS
        self.solution = Solution(graph)
        self.modularity = Modularity(graph)
        self.new_solution = deepcopy(self.solution)
        self.temp_solution = deepcopy(self.solution)
    
    def my_shuffle(self, array):
        random.shuffle(array)
        return array

    def find(self):
        if self.VERBOSE: print("(FS) START Finding solutions for all vertices")
        random_vertices = self.my_shuffle(list(self.graph.vertices))
        for vertex in random_vertices:
            if self.DEBUG: print("--------------------SOLO-------------------")
            if self.DEBUG: print("(FS) Finding new solution for vertex", vertex)
            string_vertex = str(vertex)

            # add just the vertex to the solution
            solo_community = [vertex]
            self.solution.communities.append(solo_community)
            # update solo vertex's solution community
            solo_community_index = self.solution.communities.index(
                solo_community)
            self.solution.vertices_communities[string_vertex] = solo_community_index

            # find density
            solo_density = self.modularity.calculate_density_signed(
                self.solution, self.LAMBDA)

            current_best_density = solo_density
            current_best_community = solo_community_index
            if self.DEBUG: print("(FS) DEBUG Current communities: ", self.solution.communities)
            if self.DEBUG: print("(FS) DEBUG Current best density for: ", vertex, "is", solo_density)
            if self.DEBUG: print("(FS) DEBUG Current best community for: ", vertex, "is", solo_community_index)
            if self.DEBUG: print("(FS) DEBUG Current vertices communities relation: ", self.solution.vertices_communities)

            self.new_solution = deepcopy(self.solution)
            for community_index, community in enumerate(self.new_solution.communities):
                if self.DEBUG: print("--------------------GROUPING-------------------")
                if self.DEBUG:  print("(FS) Trying new communities for vertex", vertex, "at community", community_index)
                self.temp_solution = deepcopy(self.new_solution)

                # if there is only ONE community, is the first step
                if (len(self.solution.communities) < 2):
                    if self.DEBUG: print("(FS) DEBUG Only 1 community yet")
                    continue

                # if it's the same solo community, ignore
                if (community == solo_community):
                    if self.DEBUG: print("(FS) DEBUG  Its same solo community. Ignoring...")
                    continue

                # start by removing vertex from any community
                vertex_community = self.temp_solution.get_community_index(
                    vertex)
                if self.DEBUG: print("(FS) DEBUG Current vertex community", vertex_community)
                if (vertex_community != None):
                    self.temp_solution.communities[vertex_community].remove(
                        vertex)
                    if self.DEBUG: print("(FS) DEBUG Removing vertex from its current community to try others", self.temp_solution.communities)

                # add vertex to a new community
                self.temp_solution.communities[community_index].append(
                    vertex)
                self.temp_solution.vertices_communities[vertex] = community_index

                # calculate new density
                new_density = self.modularity.calculate_density_signed(
                    self.temp_solution, self.LAMBDA)
                if self.DEBUG: print("(FS) DEBUG New density with community", community_index, "Density:", new_density)
                if self.DEBUG: print("(FS) DEBUG New solution communities: ",
                   self.temp_solution.communities)

                # in case it finds a better community, save it
                if (new_density > current_best_density):
                    if self.DEBUG: print("(FS) DEBUG Best solution for", vertex, "found", self.temp_solution.communities,
                        "Density: ", new_density)
                    current_best_density = new_density
                    current_best_community = community_index
                    self.solution = deepcopy(self.temp_solution)
                # else: TODO check if it is needed
                #     print("(FS) Previous density was better", current_best_density, "Continuing...")
            if self.DEBUG: print("--------------------")
            if self.DEBUG: print("(FS) DEBUG Current communities: ", self.solution.communities)
            if self.DEBUG: print("(FS) DEBUG Current best density for: ", vertex, "is", solo_density)
            if self.DEBUG: print("(FS) DEBUG Current best community for: ", vertex, "is", solo_community_index)
            if self.DEBUG: print("(FS) DEBUG Current vertices communities relation: ", self.solution.vertices_communities)
        if self.DEBUG: print("--------------------")
        final_density = self.modularity.calculate_density_signed(
            self.solution, self.LAMBDA)

        if self.VERBOSE: print("Solution density: ", final_density)
        if self.VERBOSE: print("Solution communities: ", self.solution.communities)
        return self.solution
