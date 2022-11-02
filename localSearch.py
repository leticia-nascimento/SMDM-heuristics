from solution import Solution


class LocalSearch:
    def __init__(self, graph):
        self.graph = graph
        self.solutions = []

    def createSolutions(self):
        for vertice in self.graph.vertices:
            # starting with n vertices n solutions
            self.solutions.append([vertice])
            for next_vertice in self.graph.vertices:
                self.solutions.append([vertice])
