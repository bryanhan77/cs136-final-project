import graph_io
import sys

from match import chain_cycle_match, get_match_list

from transport import Input

MAX_CHAIN_LENGTH = 3
MAX_CYCLE_LENGTH = 3


def solve(input, algo):
    graph, weights, ndds, node_names = graph_io.generate_graph(input)
    input_data = Input(graph, weights, ndds, MAX_CYCLE_LENGTH, MAX_CHAIN_LENGTH)
    result = chain_cycle_match(input_data, algo)
    if result:
        output_data, formulation = result
        cycle_chains_list = get_match_list(output_data, graph, weights)
        return cycle_chains_list, formulation, input_data, output_data, node_names


if __name__ == '__main__':
    input, output, algo = sys.argv[1:4]
    print("Input: " + input)
    print("Output: " + output)

    graph, weights, ndds, node_names = graph_io.generate_graph(input)
    input_data = Input(graph, weights, ndds, MAX_CYCLE_LENGTH, MAX_CHAIN_LENGTH)
    result = chain_cycle_match(input_data, algo)
    if result:
        output_data, formulation = result
        cycle_chains_list = get_match_list(output_data, graph, weights)
    result = cycle_chains_list, formulation, input_data, output_data, node_names
    if result:
        graph_io.write_to_csv(cycle_chains_list, output, node_names)