from solution import Solution
from local_search import LocalSearch
from find_solutions import FindSolutions
from modularity import Modularity
from copy import deepcopy


class Grasp:
    def __init__(self, graph, LAMBDA):
        self.graph = graph
        self.LAMBDA = LAMBDA
        self.solution = Solution(graph)
        self.modularity = Modularity(graph)

    def find_solution(self):
        print("(Grasp) START Finding best solution")

        find_solutions = FindSolutions(self.graph, self.LAMBDA)
        first_solution = find_solutions.find()

        local_search = LocalSearch(self.graph, first_solution, self.LAMBDA)
        second_solution = local_search.search()

        return self.solution.communities
