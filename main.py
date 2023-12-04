import sys

def parse(file):
    ndds = []
    pairs = []
    edges = []

    with open(file) as f:
        num_ndds = f.readline()
        for i in range(num_ndds):
            ndds.append(f.readline())
        
        num_pairs = f.readline()
        for i in range(num_pairs):
            pairs.append(f.readline().split(','))
        
        num_edges = f.readline()
        for i in range(num_edges):
            edges.append(f.readline().split(','))

    return ndds, pairs, edges

def run(input_graph, algo):
    pass


if __name__ == '__main__':
    input_file = sys.args[1]
    algo = sys.args[2]

    ndds, pairs, edges = parse(input_file)

    result = run(ndds, pairs, edges, algo)

    # TODO: more sophisticated printing of results
    print(result)

