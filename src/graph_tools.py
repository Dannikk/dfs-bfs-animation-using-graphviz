from celluloid import Camera
import src.graph_reader as gr
from src.algorithms import *

DEFAULT_COLOR = 'blue'
MARKED_COLOR = 'green'
FILE_NAME_TEMPLATE = ' animation '
EXTENSION = '.gif'
FRAME_INTERVAL = 600
NODE_SIZE = 500


def graph_builder(file_path: str) -> nx.Graph:
    """
    Function that construct networkx.Graph using generator

    Parameters
    ----------
    file_path : str
        directory to file to read graph

    Returns
    -------
    `~networkx.Graph` :
        graph constructing from the text file located in file_path

    """
    graph = nx.DiGraph()
    for nod, neighs in gr.read_graph(file_path):
        for neighbour in neighs:
            graph.add_edge(nod, neighbour)
    return graph


def create_gif(graph: nx.Graph, camera: Camera, start: object, storage: str,
               func: str = 'dfs', source: str = '') -> bool:
    """
    Function that create a gif file using Camera from celluloid

    Parameters
    ----------
    graph : `~networkx.Graph`
        any graph
    camera : Camera
        Camera class object required to create the file
    start : object
        any hashable object that is the start node
    storage : str
        directory where you want to save the gif file
    func : str, default: 'dfs'
        the name of the algorithm you want to apply to the graph
    source : str, default: ''
        directory to the file in which the graph was located
        it's required for title and name of the .gif file

    Returns
    -------
    bool :
        True if the file was created and no errors occurred,
        False otherwise

    """
    functions = {'dfs': lambda start_point: dfs(graph, start),
                 'bfs': lambda start_point: bfs(graph, start)}

    file_name = storage + func + FILE_NAME_TEMPLATE + '(' + source.replace('/', '.') + ')' + EXTENSION
    nodes_color = [graph.nodes[node].get('color', DEFAULT_COLOR) for node in graph.nodes()]
    nx.draw_planar(graph, with_labels=True, node_size=NODE_SIZE,
                   node_color=nodes_color)
    camera.snap()

    try:
        for node in functions.get(func)(start):
            graph.nodes[node]['color'] = MARKED_COLOR
            nodes_color = [graph.nodes[node].get('color', DEFAULT_COLOR) for node in graph.nodes()]
            nx.draw_planar(graph, with_labels=True, node_size=NODE_SIZE,
                           node_color=nodes_color)
            camera.snap()
    except ValueError:
        return False
    animation = camera.animate(FRAME_INTERVAL)
    animation.save(file_name, writer='imagemagick')
    return True
