from solution import Solution
from local_search import LocalSearch
from find_solutions import FindSolutions
from modularity import Modularity
from copy import deepcopy


class Grasp:
    def __init__(self, graph, LAMBDA, m):
        self.graph = graph
        self.LAMBDA = LAMBDA
        self.best_solution = Solution(graph)
        self.modularity = Modularity(graph)
        self.m = m # quantidade de soluções que serão criadas

    def find_solution(self):
        print("(Grasp) START Finding best solution")

        for index in range(self.m):
            print("DEBUG: loop numero", index)
            find_solutions = FindSolutions(self.graph, self.LAMBDA)
            first_solution = find_solutions.find()

            local_search = LocalSearch(self.graph, first_solution, self.LAMBDA)
            second_solution = local_search.search()

            print("DEBUG: best_solution", self.best_solution.density)
            print("DEBUG: second_solution", second_solution.density)
            if (self.best_solution.density < second_solution.density):
                self.best_solution = deepcopy(second_solution)

        return self.best_solution
