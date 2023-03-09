from graph import Graph
from modularity import Modularity
from solution import Solution
from grasp import Grasp
from local_search import LocalSearch
from find_solutions import FindSolutions
import argparse
import numpy
import time


def main():
    text = "Example: \n\
                main.py identification 0.5 datasets/rudson.net"
    parser = argparse.ArgumentParser(
        description=text, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("id", help="set graph identification")
    parser.add_argument(
        "lbda", help="set lambda value between 0,5 and 1")  # confirmar
    parser.add_argument("dataset", help="set input data")

    args = parser.parse_args()

    ID = args.id
    DATASET = args.dataset
    LAMBDA = float(args.lbda)
    graph = Graph(ID)
    graph.read_file(DATASET)
    start_time = time.time()

    print('(Config) File: ', DATASET)
    print('(Config) Identification: ', ID)
    print('(Config) Lambda: ', LAMBDA)
    print('----------------')
    print('(G) Edges: ', graph.edges)
    print('(G) Edges Size: ', graph.num_edges())
    print('(G) Vertices: ', graph.vertices)
    print('(G) Vertices Size: ', graph.num_vertices())
    print('(G) Degrees: ', graph.degrees)

    modularity = Modularity(graph)
    solution = Solution(graph)

    # DEBUG gakuhu 0.5
    # solution.add_communities(
    #     [[16], [5, 14], [3, 4, 6, 7, 8, 11, 12], [9, 10, 13], [1, 2], [15]]
    # )

    # DEBUG parlamento 0.8
    # solution.add_communities(
    #     [[10], [7], [5], [2], [4], [1], [3], [6], [8], [9]]
    # )

    # print('----------------')
    # print('(S) Communities: ', solution.communities)
    # print('(S) Vertices by Communities: ', solution.vertices_communities)
    # density = modularity.calculate_density_signed(solution, LAMBDA)
    # print('(S) Density: ', density)

    # print('----------------')
    # local_search = LocalSearch(graph, solution, LAMBDA)
    # best_neighbour = local_search.search()

    # print('----------------')
    # find_solutions = FindSolutions(graph, LAMBDA)
    # found_solution = find_solutions.find()
    # print('(SL) Solution found: ', found_solution.density)

    print('----------------')
    grasp = Grasp(graph, LAMBDA, 5)
    solution = grasp.find_solution()
    print('(GR) Solution found: ', solution.communities)
    print('(GR) Solution found density: ', solution.density)

    print('----------------')
    print("(Execution) Execution time:")
    print("%s seconds" % (time.time() - start_time))


if __name__ == "__main__":
    main()
