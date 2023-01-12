from solution import Solution
from modularity import Modularity
from copy import deepcopy

# Obter a solução ótima local S'
# Fazer um shuffle dos vertices e cortar pra fazer uma solução aleatoria


class LocalSearch:
    def __init__(self, graph, solution, LAMBDA):
        self.graph = graph
        self.LAMBDA = LAMBDA
        self.solution = solution
        self.modularity = Modularity(graph)
        self.best_neighbour = deepcopy(solution)

    # Para a melhor solução, encontrar uma lista de todos os vizinhos possíveis até encontrar
    # alguém melhor
    def find_best_neighbour(self):
        print("(LS) Finding best neighbour for current best neighbour: ", self.best_neighbour.communities)
        temp_solution = deepcopy(self.best_neighbour)

        for community_index, community in enumerate(self.best_neighbour.communities):
            for vertice_index in range(len(community)):
                temp_solution = deepcopy(self.best_neighbour)

                # Vertice info
                vertice = community[vertice_index]
                string_vertice = str(vertice)
                vertice_community = community_index
                print("(LS) DEBUG vertice: ", vertice)

                for next_community_index, next_community in enumerate(self.best_neighbour.communities):
                    # Remove da comunidade antiga
                    temp_solution.communities[vertice_community].remove(vertice)

                    # Adiciona na comunidade nova
                    temp_solution.communities[next_community_index].append(vertice)
                    temp_solution.vertices_communities[string_vertice] = next_community_index
                    vertice_community = next_community_index

                    print("(LS) DEBUG temp_solution.communities: ", temp_solution.communities)
                    print("(LS) DEBUG temp_solution.vertices_communities: ", temp_solution.vertices_communities)

                    # Calcula nova densidade
                    temp_density = self.modularity.calculate_density_signed(temp_solution, self.LAMBDA)
                    print("(LS) DEBUG temp_density: ", temp_density)

                    if (temp_density > self.best_neighbour.density):
                       print("(LS) New best density found: ", self.best_neighbour.communities)
                       self.best_neighbour = deepcopy(self.solution)
                       return self.best_neighbour

        print("(LS) Best neighbour not found. Keeping solution: ", self.best_neighbour.communities)
        return self.best_neighbour

    def search(self):
        print("(LS) START Find best neighbour for: ", self.solution.communities)

        # 1.	solucaoVizinha = copy(solucao_inicial)
        # 2.	faça{
        # 3.	.	solucao        = copy(solucaoVizinha)
        # 4.	.	solucaoVizinha = melhorVizinho(solucao)
        # 5.	}enquanto mod(solucaoVizinha) melhor que mod(solucao);
        # 6.	return solucao

        while (self.find_best_neighbour().density > self.solution.density):
            self.find_best_neighbour()

        print("(LS) Final solution: ",
            "\n - Communities: ", self.best_neighbour.communities,
            "\n - Density: ", self.best_neighbour.density)
        return self.best_neighbour
