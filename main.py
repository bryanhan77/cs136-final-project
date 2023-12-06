import sys

from match import chain_cycle_match, get_match_list, get_formulation, print_options

def parse(file):
    ndds = []
    pairs = []
    edges = []

    with open(file) as f:
        num_ndds = f.readline()
        for i in range(int(num_ndds)):
            ndds.append(f.readline())
        
        num_pairs = f.readline()
        for i in range(int(num_pairs)):
            pairs.append(f.readline().split(','))
        
        num_edges = f.readline()
        for i in range(int(num_edges)):
            edges.append(f.readline().split(','))

    return ndds, pairs, edges

def run(input_graph, algo):
    # if max_cycle_length is None:
    #     max_cycle_length = problem_data["max_cycle_length"]
    # if max_chain_length is None:
    #     max_chain_length = problem_data["max_chain_length"]
    max_cycle_length = 2
    max_chain_length = 3

    input_data = (ndds, pairs, edges, max_cycle_length, max_chain_length)
    result = chain_cycle_match(ndds, pairs, edges, algo)
    if result is None:
        return None
    output_data, formulation = result
    cycle_chains_list = get_match_list(output_data, graph, weights)
    return cycle_chains_list, formulation, input_data, output_data, node_names


if __name__ == '__main__':
    input_file = sys.argv[1]
    solver = sys.argv[2]

    ndds, pairs, edges = parse(input_file)

    print(ndds, pairs, edges)

    result = run(ndds, pairs, edges, solver)

    # TODO: more sophisticated printing of results
    print(result)

