from solution import Solution
from local_search import LocalSearch
from find_solutions import FindSolutions
from modularity import Modularity
from copy import deepcopy


class Grasp:
    def __init__(self, graph, LAMBDA, M, VERBOSE, DEBUG_FIND_SOLUTIONS, DEBUG_LOCAL_SEARCH):
        self.graph = graph
        self.LAMBDA = LAMBDA
        self.M = M
        self.VERBOSE = VERBOSE
        self.DEBUG_FIND_SOLUTIONS = DEBUG_FIND_SOLUTIONS
        self.DEBUG_LOCAL_SEARCH = DEBUG_LOCAL_SEARCH
        self.best_solution = Solution(graph)
        self.modularity = Modularity(graph)

    def find_solution(self):
        print("(Grasp) START Finding best solution... this may take a while.")
        for index in range(self.M):
            if self.VERBOSE: print("--------------------")
            if self.VERBOSE: print("GR: Solution", index + 1)

            find_solutions = FindSolutions(self.graph, self.LAMBDA, self.VERBOSE, self.DEBUG_FIND_SOLUTIONS)
            first_solution = find_solutions.find()

            local_search = LocalSearch(self.graph, first_solution, self.LAMBDA, self.VERBOSE, self.DEBUG_LOCAL_SEARCH)
            second_solution = local_search.search()

            if (self.best_solution.density < second_solution.density):
                self.best_solution = deepcopy(second_solution)

        return self.best_solution
