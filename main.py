from graph import Graph
from modularity import Modularity
from solution import Solution
import argparse


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

    print('Edges: ', graph.edges)
    print('Edges Size: ', graph.num_edges())
    print('Vertices: ', graph.vertices)
    print('Vertices Size: ', graph.num_vertices())
    print('Degrees: ', graph.degrees)
    print('Degree: ', graph.get_degree('1'))

    modularity = Modularity(graph)
    solution = Solution(graph)

    # nossoHeuristics_GT
    solution.add_communities(
        [[10], [14], [2, 3, 6, 7], [15], [0], [1],
            [5], [11], [4], [8], [9], [12], [13]]
    )

    density = modularity.calculateDensitySigned(solution, LAMBDA)
    print('Density: ', density)


if __name__ == "__main__":
    main()
