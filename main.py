from graph import Graph
from modularity import Modularity
from solution import Solution
from grasp import Grasp
from local_search import LocalSearch
from find_solutions import FindSolutions
import argparse
import numpy
import time


def print_execution_time(start_time):
    print('----------------')
    print("(Execution) Execution time:")
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    execution_time_in_ms = execution_time * 1000
    print(execution_time_in_ms, "milliseconds")
    print(execution_time, "seconds")


def debug_find_solutions(graph, LAMBDA):
    print('----------------')
    find_solutions = FindSolutions(graph, LAMBDA, True, True)
    found_solution = find_solutions.find()
    print('(SL) Solution found: ', found_solution.density)


def debug_local_search(graph, solution, LAMBDA):
    # gahuku 0.5
    solution.add_communities(
        [[16], [5, 14], [3, 4, 6, 7, 8, 11, 12], [9, 10, 13], [1, 2], [15]]
    )
    print('----------------')
    local_search = LocalSearch(graph, solution, LAMBDA, True, True)
    best_neighbor = local_search.search()
    print('(LS) Best local: ', best_neighbor.density)


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
        "-v", help="verbose mode", action='store_true')
    parser.add_argument(
        "-d", help="full debug mode", action='store_true')
    parser.add_argument(
        "-l", help="debug local search mode", action='store_true')
    parser.add_argument(
        "-f", help="debug find solution mode", action='store_true')
    parser.add_argument(
        "-lo", help="debug local search mode", action='store_true')
    parser.add_argument(
        "-fo", help="debug find solution mode", action='store_true')

    start_time = time.perf_counter()
    args = parser.parse_args()
    ID = args.id
    DATASET = args.dataset
    LAMBDA = float(args.lbda)
    M = int(args.m)
    VERBOSE = args.v
    DEBUG = args.d
    DEBUG_FIND_SOLUTIONS = args.f or DEBUG
    DEBUG_LOCAL_SEARCH = args.l or DEBUG
    DEBUG_FIND_SOLUTIONS_ONLY = args.fo
    DEBUG_LOCAL_SEARCH_ONLY = args.lo
    graph = Graph(ID)
    graph.read_file(DATASET)

    print('(Config) File: ', DATASET)
    print('(Config) Identification: ', ID)
    print('(Config) Lambda: ', LAMBDA)
    print('(Config) M: ', M)
    print('(Config) Verbose mode: ', VERBOSE)
    print('(Config) Debug mode: ', DEBUG)
    print('(Config) Debug find solutions: ', DEBUG_FIND_SOLUTIONS)
    print('(Config) Debug local search: ', DEBUG_LOCAL_SEARCH)
    print('(Config) Debug find solutions ONLY: ', DEBUG_FIND_SOLUTIONS_ONLY)
    print('(Config) Debug local search ONLY: ', DEBUG_LOCAL_SEARCH_ONLY)
    print('----------------')
    print('(G) Edges: ', graph.edges)
    print('(G) Edges Size: ', graph.num_edges())
    print('(G) Vertices: ', graph.vertices)
    print('(G) Vertices Size: ', graph.num_vertices())
    print('(G) Degrees: ', graph.degrees)

    solution = Solution(graph)

    if DEBUG_LOCAL_SEARCH_ONLY:
        debug_local_search(graph, solution, LAMBDA)
        print_execution_time(start_time)
        return 0
    
    if DEBUG_FIND_SOLUTIONS_ONLY:
        debug_find_solutions(graph, LAMBDA)
        print_execution_time(start_time)
        return 0

    print('----------------')
    grasp = Grasp(graph, LAMBDA, M, VERBOSE, DEBUG_FIND_SOLUTIONS, DEBUG_LOCAL_SEARCH)
    solution = grasp.find_solution()
    print("--------------------")
    print('(GR) Solution found: ', solution.communities)
    print('(GR) Solution found density: ', solution.density)
    
    print_execution_time(start_time)


if __name__ == "__main__":
    main()
