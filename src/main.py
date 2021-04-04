import networkx as nx
import matplotlib.pyplot as plt
from celluloid import Camera
import src.graph_reader as gr


DEFAULT_COLOR = 'blue'
MARKED_COLOR = 'green'
graph = nx.DiGraph()
fig = plt.figure()
camera = Camera(fig)


for nod, neighs in gr.read_graph('graph.txt'):
    # print(nod, neighs)
    for neighbour in neighs:
        graph.add_edge(nod, neighbour)

nx.draw_circular(graph, with_labels=True,
                 node_color=[graph.nodes[node].get('color', DEFAULT_COLOR) for node in graph.nodes()])
camera.snap()

for _, attrs in graph.nodes.items():
    attrs['color'] = MARKED_COLOR
    nc = [graph.nodes[node].get('color', DEFAULT_COLOR) for node in graph.nodes()]
    # print("nc=", nc)
    nx.draw_circular(graph, with_labels=True,
                     node_color=[graph.nodes[node].get('color', DEFAULT_COLOR) for node in graph.nodes()])
    camera.snap()

animation = camera.animate(interval=600)
animation.save("anim_graph.gif", writer="imagemagick")
