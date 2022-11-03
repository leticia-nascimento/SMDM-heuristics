
class Modularity:
    def __init__(self, graph):
        self.graph = graph

    def calculate_density_signed(self, solution, lbda):
        density = 0.0
        for community in solution.communities:
            edgesPlus = 0.0
            edgesMinus = 0.0
            totalDegreePlus = 0.0
            totalDegreeMinus = 0.0
            for vertice_index in range(len(community)):
                vertice = str(community[vertice_index])
                totalDegreePlus += self.graph.get_positive_degree(vertice)
                totalDegreeMinus += self.graph.get_negative_degree(vertice)

                for neighbour in self.graph.get_neighbours(vertice):
                    if (solution.get_weight((vertice, neighbour)) > 0.0):
                        edgesPlus += solution.get_weight(
                            (vertice, neighbour))
                    if (solution.get_weight((vertice, neighbour)) < 0.0):
                        edgesMinus += solution.get_weight((vertice,
                                                            neighbour)) * -1.0
            nnodes = len(community)
            if (nnodes > 0.0):
                density += (4.0 * lbda * edgesPlus - (2 - 2 * lbda) * (totalDegreePlus - 2 * edgesPlus)
                            - (2.0 - 2.0 * lbda) * 2.0 * edgesMinus + 2.0 *
                            lbda * (totalDegreeMinus - 2.0 * edgesMinus)
                            ) / nnodes
        solution.density = density
        return density
