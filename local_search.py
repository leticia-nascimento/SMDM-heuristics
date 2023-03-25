from solution import Solution
from modularity import Modularity
from copy import deepcopy

# Find the best local solution S'
# To the current best solution, find a list of all possible neighbors until finding a better solution
class LocalSearch:
    def __init__(self, graph, solution, LAMBDA, VERBOSE, DEBUG_LOCAL_SEARCH):
        self.graph = graph
        self.LAMBDA = LAMBDA
        self.VERBOSE = VERBOSE
        self.DEBUG = DEBUG_LOCAL_SEARCH
        self.solution = solution
        self.modularity = Modularity(graph)
        self.best_neighbor = deepcopy(solution)

    def find_best_neighbor(self):
        if self.VERBOSE: print("(LS) Finding best neighbor for current best neighbor: ", self.best_neighbor.communities)
        temp_solution = deepcopy(self.best_neighbor)

        for community_index, community in enumerate(self.best_neighbor.communities):
            for vertex_index in range(len(community)):
                temp_solution = deepcopy(self.best_neighbor)

                # vertex info
                vertex = community[vertex_index]
                string_vertex = str(vertex)
                vertex_community = community_index
                if self.DEBUG: print("(LS) DEBUG vertex: ", vertex)

                for next_community_index, next_community in enumerate(self.best_neighbor.communities):
                    # remove vertex from current community
                    temp_solution.communities[vertex_community].remove(vertex)

                    # add vertex to a new community
                    temp_solution.communities[next_community_index].append(vertex)
                    temp_solution.vertices_communities[string_vertex] = next_community_index
                    vertex_community = next_community_index

                    if self.DEBUG: print("(LS) DEBUG temp_solution.communities: ", temp_solution.communities)
                    if self.DEBUG: print("(LS) DEBUG temp_solution.vertices_communities: ", temp_solution.vertices_communities)

                    # calculate new density
                    temp_density = self.modularity.calculate_density_signed(temp_solution, self.LAMBDA)
                    if self.DEBUG: print("(LS) DEBUG temp_density: ", temp_density)

                    # in case it finds a better neighbor, return it
                    if (temp_density > self.best_neighbor.density):
                       if self.VERBOSE: print("(LS) New best density found: ", self.best_neighbor.communities)
                       self.best_neighbor = deepcopy(self.solution)
                       return self.best_neighbor

        if self.VERBOSE: print("(LS) Best neighbor not found. Keeping solution: ", self.best_neighbor.communities)
        return self.best_neighbor

    def search(self):
        if self.VERBOSE: print("(LS) START Find best neighbor for: ", self.solution.communities)

        # 1.	solucaoVizinha = copy(solucao_inicial)
        # 2.	faça{
        # 3.	.	solucao        = copy(solucaoVizinha)
        # 4.	.	solucaoVizinha = melhorVizinho(solucao)
        # 5.	}enquanto mod(solucaoVizinha) melhor que mod(solucao);
        # 6.	return solucao

        while (self.find_best_neighbor().density > self.solution.density):
            self.find_best_neighbor()

        if self.VERBOSE: print("(LS) Final solution: ",
            "\n - Communities: ", self.best_neighbor.communities,
            "\n - Density: ", self.best_neighbor.density)
        return self.best_neighbor
