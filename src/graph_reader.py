import os

DELIMITER = ':'
NODES_DELIMITER = ','


def read_graph(file_path: str):
    """
    Function that reads a graph from a text file

    Parameters
    ----------
    file_path : str
        directory to file to read graph

    Returns
    -------
    generator :
        yielding node (any hashable object), list of neighbors
    """
    with open(file_path, 'r') as file:
        for line in file:
            node, _, neighbors = line.partition(DELIMITER)
            assert neighbors
            yield node, neighbors.replace(NODES_DELIMITER, '').split()
