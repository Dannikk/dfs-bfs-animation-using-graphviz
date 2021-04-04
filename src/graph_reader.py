
DELIMITER = ':'
NODES_DELIMITER = ','


def read_graph(file_path: str):
    with open(file_path, 'r') as file:
        for line in file:
            node, _, neighbors = line.partition(DELIMITER)
            assert neighbors
            yield node, neighbors.replace(NODES_DELIMITER, '').split()
