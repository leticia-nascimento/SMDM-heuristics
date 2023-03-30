from graph import Graph
from modularity import Modularity
from solution import Solution
from grasp import Grasp
from local_search import LocalSearch
from find_solutions import FindSolutions
import argparse
import numpy
import time
import csv

from subprocess import call
import pdb
from multiprocessing import Pool, cpu_count

#detect how many processes will run at the same time
try:
    workers = cpu_count()-1
except NotImplementedError:
    workers = 1

#initialize pool of processes
processes = []


def print_execution_time(start_time):
    print('----------------')
    print("(Execution) Execution time:")
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    execution_time_in_ms = execution_time * 1000
    print(execution_time_in_ms, "milliseconds")
    print(execution_time, "seconds")
    return [execution_time_in_ms, execution_time]


def debug_find_solutions(graph, LAMBDA):
    print('----------------')
    find_solutions = FindSolutions(graph, LAMBDA, True, True)
    found_solution = find_solutions.find()
    print('(FS) Final density: ', found_solution.density)


def debug_local_search(graph, solution, LAMBDA):
    # gahuku 0.5
    solution.add_communities(
        [[16], [5, 14], [3, 4, 6, 7, 8, 11, 12], [9, 10, 13], [1, 2], [15]]
    )
    modularity = Modularity(graph)
    solution.density = modularity.calculate_density_signed(solution, LAMBDA)
    print("(LS) DEBUG Solution density:", solution.density)
    print('----------------')
    local_search = LocalSearch(graph, solution, LAMBDA, True, True)
    best_neighbor = local_search.search()
    print('(LS) Best local: ', best_neighbor.density)

# [0]graph, [1]lambd, [2]M, [3]VERBOSE, [4]DEBUG_FIND_SOLUTIONS, [5]DEBUG_LOCAL_SEARCH, [6]start_time, [7]DATASET, [8]num_vertices, [9]num_edges]
def execute_grasp(args):

    with open("testeee.csv", 'w', newline='') as file:
        # columns = ["file_name","vertices","edges","m","lambda","density","time_ms", "time_s"]
        writer = csv.writer(file)
        # writer.writerow(columns)

        print('----------------')
        grasp = Grasp(args[0], args[1], args[2], args[3], args[4], args[5])
        solution = grasp.find_solution()
        print("--------------------")
        print('(GR) Solution found: ', solution.communities)
        print('(GR) Solution found density: ', solution.density)

        end_time = time.perf_counter()
        execution_time = end_time - args[6]
        execution_time_in_ms = execution_time * 1000
        writer.writerow([args[7], args[8], args[9], args[2], args[1], solution.density, execution_time_in_ms, execution_time])


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
    parser.add_argument(
        "-p", help="parallel execution mode", action='store_true')

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
    PARALLEL = args.p
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

    if not PARALLEL:
        repeat = 2 # number of executions per config
        columns = ["file_name","vertices","edges","m","lambda","density","time_ms", "time_s"]
        lambds = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9] # lambda values to test for a file and M

        with open(ID + ".csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(columns)
            for i in range(repeat):
                for lambd in lambds:
                    print('----------------')
                    grasp = Grasp(graph, LAMBDA, M, VERBOSE, DEBUG_FIND_SOLUTIONS, DEBUG_LOCAL_SEARCH)
                    solution = grasp.find_solution()
                    print("--------------------")
                    print('(GR) Solution found: ', solution.communities)
                    print('(GR) Solution found density: ', solution.density)

                    end_time = time.perf_counter()
                    execution_time = end_time - start_time
                    execution_time_in_ms = execution_time * 1000
                    writer.writerow([DATASET, graph.num_vertices(), graph.num_edges(), M, lambd, solution.density, execution_time_in_ms, execution_time])
        print_execution_time(start_time)
            
    else:
        repeat = 2 # number of executions per config
        columns = ["file_name","vertices","edges","m","lambda","density","time_ms", "time_s"]
        lambds = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9] # lambda values to test for a file and M
        lines = 1 + (len(lambds) * repeat)
        print ("Total lines", lines)

        with open("teste.csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(columns)

        for i in range(repeat):
            for lambd in lambds:
                processes.append([graph, lambd, M, VERBOSE, DEBUG_FIND_SOLUTIONS, DEBUG_LOCAL_SEARCH, start_time, DATASET, graph.num_vertices(), graph.num_edges()])
                # [0]graph, [1]lambd, [2]M, [3]VERBOSE, [4]DEBUG_FIND_SOLUTIONS, [5]DEBUG_LOCAL_SEARCH, [6]start_time, [7]DATASET, [8]num_vertices, [9]num_edges]

        # print ("Total processes:{}".format(len(processes)),processes)
        # call the processes
        pool = Pool(processes=workers)
        result = pool.map(execute_grasp, processes)
        print("RESULT", result)
        print_execution_time(start_time)
        pool.close()


if __name__ == "__main__":
    main()
