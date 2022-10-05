from graph import Graph
import argparse


def main():
    text = "Example: \n\
                main.py identification datasets/rudson.net"
    parser = argparse.ArgumentParser(
        description=text, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("id", help="set graph identification")
    parser.add_argument("dataset", help="set input data")

    args = parser.parse_args()

    ID = args.id
    DATASET = args.dataset
    graph = Graph(ID)
    print(DATASET)
    graph.read_file(DATASET)

    print('Edges: ', graph.edges)
    print('Edges Size: ', graph.num_edges())
    print('Vertices: ', graph.vertices)
    print('Vertices Size: ', graph.num_vertices())


if __name__ == "__main__":
    main()
