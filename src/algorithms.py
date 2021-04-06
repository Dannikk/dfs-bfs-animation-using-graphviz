import networkx as nx
from queue import LifoQueue, Queue


def dfs(graph: nx.Graph, start: object):
    """
    Non-recursive realization of depth-first search algorithm using `~queue.LifoQueue`

    Parameters
    ----------
    graph : `~networkx.Graph`
        any graph
    start : object
        any hashable object

    Returns
    -------
    generator :
        yielding node by node of dfs path, on None in error case
    """

    if start not in list(graph.nodes()):
        raise ValueError("\nThe graph does not contain such a node"
                         "Set the correct node")

    stack = LifoQueue(graph.number_of_nodes())
    stack.put(start)
    visited = set()
    while not stack.empty():
        current = stack.get()
        if current in visited:
            continue
        visited.add(current)
        yield current

        for neighbor in graph.neighbors(current):
            if neighbor not in visited:
                stack.put(neighbor)


def bfs(graph: nx.Graph, start: object):
    """
    Non-recursive realization of breadth-first search algorithm using `~queue.Queue`

    Parameters
    ----------
    graph : `~networkx.Graph`
        any graph
    start : object
        any hashable object

    Returns
    -------
    generator :
        yielding node by node of bfs path, on None in error case
    """
    if start not in list(graph.nodes()):
        raise ValueError("\nThe graph does not contain such a node"
                         "Set the correct node")

    queue = Queue()
    queue.put(start)
    visited = set()
    while not queue.empty():
        current = queue.get()
        if current in visited:
            continue
        visited.add(current)
        yield current

        for neighbor in graph.neighbors(current):
            if neighbor not in visited:
                queue.put(neighbor)
