from solution import Solution
from modularity import Modularity
from copy import deepcopy

# Obter a solução ótima local S'
# Fazer um shuffle dos vertices e cortar pra fazer uma solução aleatoria


class LocalSearch:
    def __init__(self, graph, solution, LAMBDA, DEBUG):
        self.graph = graph
        self.LAMBDA = LAMBDA
        self.DEBUG = DEBUG
        self.solution = solution
        self.modularity = Modularity(graph)
        self.best_neighbor = deepcopy(solution)

    # Para a melhor solução, encontrar uma lista de todos os vizinhos possíveis até encontrar
    # alguém melhor
    def find_best_neighbor(self):
        if self.DEBUG: print("(LS) Finding best neighbor for current best neighbor: ", self.best_neighbor.communities)
        temp_solution = deepcopy(self.best_neighbor)

        for community_index, community in enumerate(self.best_neighbor.communities):
            for vertice_index in range(len(community)):
                temp_solution = deepcopy(self.best_neighbor)

                # Vertice info
                vertice = community[vertice_index]
                string_vertice = str(vertice)
                vertice_community = community_index
                # print("(LS) DEBUG vertice: ", vertice)

                for next_community_index, next_community in enumerate(self.best_neighbor.communities):
                    # Remove da comunidade antiga
                    temp_solution.communities[vertice_community].remove(vertice)

                    # Adiciona na comunidade nova
                    temp_solution.communities[next_community_index].append(vertice)
                    temp_solution.vertices_communities[string_vertice] = next_community_index
                    vertice_community = next_community_index

                    # print("(LS) DEBUG temp_solution.communities: ", temp_solution.communities)
                    # print("(LS) DEBUG temp_solution.vertices_communities: ", temp_solution.vertices_communities)

                    # Calcula nova densidade
                    temp_density = self.modularity.calculate_density_signed(temp_solution, self.LAMBDA)
                    # print("(LS) DEBUG temp_density: ", temp_density)

                    # Caso encontre um vizinho melhor, retorna o mesmo
                    if (temp_density > self.best_neighbor.density):
                       if self.DEBUG: print("(LS) New best density found: ", self.best_neighbor.communities)
                       self.best_neighbor = deepcopy(self.solution)
                       return self.best_neighbor

        if self.DEBUG: print("(LS) Best neighbor not found. Keeping solution: ", self.best_neighbor.communities)
        return self.best_neighbor

    def search(self):
        if self.DEBUG: print("(LS) START Find best neighbor for: ", self.solution.communities)

        # 1.	solucaoVizinha = copy(solucao_inicial)
        # 2.	faça{
        # 3.	.	solucao        = copy(solucaoVizinha)
        # 4.	.	solucaoVizinha = melhorVizinho(solucao)
        # 5.	}enquanto mod(solucaoVizinha) melhor que mod(solucao);
        # 6.	return solucao

        while (self.find_best_neighbor().density > self.solution.density):
            self.find_best_neighbor()

        if self.DEBUG: print("(LS) Final solution: ",
            "\n - Communities: ", self.best_neighbor.communities,
            "\n - Density: ", self.best_neighbor.density)
        return self.best_neighbor
