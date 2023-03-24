from solution import Solution
from local_search import LocalSearch
from find_solutions import FindSolutions
from modularity import Modularity
from copy import deepcopy


class Grasp:
    def __init__(self, graph, LAMBDA, M, DEBUG):
        self.graph = graph
        self.LAMBDA = LAMBDA
        self.M = M
        self.DEBUG = DEBUG
        self.best_solution = Solution(graph)
        self.modularity = Modularity(graph)

    def find_solution(self):
        print("(Grasp) START Finding best solution... this may take a while.")
        for index in range(self.M):
            if self.DEBUG: print("--------------------")
            if self.DEBUG: print("GR: Solution", index)

            find_solutions = FindSolutions(self.graph, self.LAMBDA, self.DEBUG)
            first_solution = find_solutions.find()

            local_search = LocalSearch(self.graph, first_solution, self.LAMBDA, self.DEBUG)
            second_solution = local_search.search()

            if (self.best_solution.density < second_solution.density):
                self.best_solution = deepcopy(second_solution)

        return self.best_solution
