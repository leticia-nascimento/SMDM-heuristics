
class Modularity:
    def __init__(self, graph):
        self.graph = graph

    def calculateDensitySigned(self, solution, lbda):
        density = 0.0
        for community in solution.communities:
            # print("community", community)
            edgesPlus = 0.0
            edgesMinus = 0.0
            totalDegreePlus = 0.0
            totalDegreeMinus = 0.0
            for vertice_index in range(len(community)):
                # vértice da comunidade
                vertice = str(community[vertice_index])
                # print("calculateDensitySigned vertice", vertice)
                # print("calculateDensitySigned vertice_index", vertice_index)
                # print("calculateDensitySigned range", range(len(community)))
                # print("totalDegreePlus", totalDegreePlus)
                # print("totalDegreeMinus", totalDegreeMinus)
                # print("edgesPlus", edgesPlus)
                # print("edgesMinus", edgesMinus)
                totalDegreePlus += self.graph.get_positive_degree(vertice)
                totalDegreeMinus += self.graph.get_negative_degree(vertice)
                for next_vertice_index in range(vertice_index + 1, len(community)):
                    # print("next_vertice_index", next_vertice_index)
                    # próximo vértice da comunidade
                    next_vertice = str(community[next_vertice_index])
                    # há adj positiva
                    if (self.graph.get_weight((vertice, next_vertice)) > 0.0):
                        edgesPlus += self.graph.get_weight(
                            (vertice, next_vertice))
                    # ha adjacencia negativa
                    if (self.graph.get_weight((vertice, next_vertice)) < 0.0):
                        edgesMinus += self.graph.get_weight((vertice,
                                                            next_vertice)) * -1.0
                    # if next_vertice_index == len(community):
                    #     break
            nnodes = len(community)
            if (nnodes > 0.0):
                density += (4.0 * lbda * edgesPlus - (2 - 2 * lbda) * (totalDegreePlus - 2 * edgesPlus)
                            - (2.0-2.0*lbda)*2.0*edgesMinus+2.0 *
                            lbda * (totalDegreeMinus - 2.0 * edgesMinus)
                            ) / nnodes
        solution.density = density
        return density


# getDegreePlus = get_positive_degree
# getDegreeMinus = get_negative_degree
# getAdj = get_adjacents == get_weight ???

# [[a, b, c], [d, e, f], [g], []]

# calculateDensitySigned
# degreeOfNodePlus
# https://github.com/rsantiago-ufsc/Signed-MDM
# https://github.com/rsantiago-ufsc/Signed-Modularity-Density-Heuristics
