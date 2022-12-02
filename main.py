from graph import Graph
from modularity import Modularity
from solution import Solution
from local_search import LocalSearch
from find_solutions import FindSolutions
import argparse
import numpy


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

    print('File: ', DATASET)
    print('Identification: ', ID)
    print('Lambda: ', LAMBDA)
    print('----------------')
    print('(G) Edges: ', graph.edges)
    print('(G) Edges Size: ', graph.num_edges())
    print('(G) Vertices: ', graph.vertices)
    print('(G) Vertices Size: ', graph.num_vertices())
    print('(G) Degrees: ', graph.degrees)
    print('----------------')

    modularity = Modularity(graph)
    solution = Solution(graph)

    # gakuhu 0.5
    # solution.add_communities(
    #     [[16], [5, 14], [3, 4, 6, 7, 8, 11, 12], [9, 10, 13], [1, 2], [15]]
    # )

        # gakuhu 0.5
    solution.add_communities(
        [[16], [5, 14], [3, 4, 6, 7, 8, 11, 12], [9, 10, 13], [1, 2], [15]]
    )

    # parlamento 0.8
    # solution.add_communities(
    #     [[10], [7], [5], [2], [4], [1], [3], [6], [8], [9]]
    # )

    print('(S) Communities: ', solution.communities)
    print('(S) Vertices by Communities: ', solution.vertices_communities)
    density = modularity.calculate_density_signed(solution, LAMBDA)
    print('(S) Density: ', density)

    # print('----------------')
    # local_search = LocalSearch(graph, solution, LAMBDA)
    # search = local_search.search()
    # print('(SL) Best density: ', search)

    print('----------------')
    find_solutions = FindSolutions(graph, LAMBDA)
    solutions = find_solutions.find()
    print('(SL) Solution found: ', solutions)


if __name__ == "__main__":
    main()
