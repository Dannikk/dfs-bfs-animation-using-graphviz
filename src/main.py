import matplotlib.pyplot as plt
from src.graph_tools import *


def main(start, file_path='../input/graph.txt', algorithm='dfs', storage: str = '../output/') -> bool:
    """
    The main function that call other functions

    Parameters
    ----------
    start : object
        any hashable object
    file_path : str
        directory to file to read graph
    algorithm : str, default: 'dfs'
        the name of the algorithm you want to apply to the graph
    storage : str, default: '../output/'
        directory where you want to save the gif file

    Returns
    -------
    bool :
        True if the file was created and no errors occurred,
        False otherwise

    """
    fig = plt.figure()
    plt.title(f'{algorithm.upper()} for graph from {file_path}')
    camera = Camera(fig)
    graph = graph_builder(file_path)
    if create_gif(graph, camera, func=algorithm, start=start, source=file_path, storage=storage):
        print("\nSuccessful completion of the program!")
        return True
    else:
        print("\nAn error has occurred!")
        return False


if __name__ == '__main__':
    main(start='A', algorithm='dfs')
