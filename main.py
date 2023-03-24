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
                main.py identification 0.5 10 datasets/rudson.net"
    parser = argparse.ArgumentParser(
        description=text, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("id", help="set graph identification")
    parser.add_argument(
        "lbda", help="set lambda value between 0,5 and 1")
    parser.add_argument(
        "m", help="quantity of solutions as integer")
    parser.add_argument("dataset", help="set input data")
    parser.add_argument(
        "-d", help="debug mode", action='store_true')

    start_time = time.perf_counter()
    args = parser.parse_args()
    ID = args.id
    DATASET = args.dataset
    LAMBDA = float(args.lbda)
    M = int(args.m)
    DEBUG = args.d
    graph = Graph(ID)
    graph.read_file(DATASET)

    print('(Config) File: ', DATASET)
    print('(Config) Identification: ', ID)
    print('(Config) Lambda: ', LAMBDA)
    print('(Config) M: ', M)
    print('(Config) Debug mode: ', DEBUG)
    print('----------------')
    print('(G) Edges: ', graph.edges)
    print('(G) Edges Size: ', graph.num_edges())
    print('(G) Vertices: ', graph.vertices)
    print('(G) Vertices Size: ', graph.num_vertices())
    print('(G) Degrees: ', graph.degrees)

    solution = Solution(graph)

    # print('----------------')
    # local_search = LocalSearch(graph, solution, LAMBDA)
    # best_neighbor = local_search.search()

    # print('----------------')
    # find_solutions = FindSolutions(graph, LAMBDA)
    # found_solution = find_solutions.find()
    # print('(SL) Solution found: ', found_solution.density)

    print('----------------')
    grasp = Grasp(graph, LAMBDA, M, DEBUG)
    solution = grasp.find_solution()
    print("--------------------")
    print('(GR) Solution found: ', solution.communities)
    print('(GR) Solution found density: ', solution.density)

    print('----------------')
    print("(Execution) Execution time:")
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    execution_time_in_ms = execution_time * 1000
    print(execution_time_in_ms, "milliseconds")
    print(execution_time, "seconds")


if __name__ == "__main__":
    main()
