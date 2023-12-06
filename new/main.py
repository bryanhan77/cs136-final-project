import graph_io
import sys

from match import chain_cycle_match, get_match_list, get_formulation

from transport import Input

MAX_CHAIN_LENGTH = 3
MAX_CYCLE_LENGTH = 3


def read_and_solve(input_path, objective_fn):
    graph, weights, ndds, node_names = graph_io.generate_graph(input_path)

    input_data = Input(graph, weights, ndds, MAX_CYCLE_LENGTH, MAX_CHAIN_LENGTH)
    result = chain_cycle_match(input_data, objective_fn)
    if result is None:
        return None
    output_data, formulation = result
    cycle_chains_list = get_match_list(output_data, graph, weights)
    return cycle_chains_list, formulation, input_data, output_data, node_names


if __name__ == '__main__':
    input_path, output_path, objective_fn = sys.argv[1], sys.argv[2] ,sys.argv[3]

    print("Input path: " + input_path)
    print("Output path: %s" % output_path)
    print("Formulation: %s" % get_formulation(objective_fn).__name__)
    result = read_and_solve(input_path, objective_fn)
    if result is None:
        sys.exit(1)
    cycle_chains_list, formulation, input_data, output_data, node_names = result
    graph_io.write_to_csv(cycle_chains_list, output_path, node_names)