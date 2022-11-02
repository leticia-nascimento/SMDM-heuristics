from graph import Graph
from modularity import Modularity
from solution import Solution
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
    print(DATASET)
    graph.read_file(DATASET)

    # print('Edges: ', graph.edges)
    # print('Edges Size: ', graph.num_edges())
    # print('Vertices: ', graph.vertices)
    # print('Vertices Size: ', graph.num_vertices())
    # print('Degrees: ', graph.degrees)

    modularity = Modularity(graph)
    solution = Solution(graph)

    # parlamento.net / lambda = 0.200000 / density 26.800000
    solution.add_communities(
        [[10], [1, 3, 6, 8, 9], [2, 4, 5, 7]]
    )

    print(solution.edges)
    print(solution.communities)
    print(solution.communities)
    print(solution.vertices_communities)
    print(solution.weights)

    density = modularity.calculateDensitySigned(solution, LAMBDA)
    print('Density: ', density)


if __name__ == "__main__":
    main()
