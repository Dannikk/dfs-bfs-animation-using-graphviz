# dfs, bfs animation using networkx

This is my student project, the task of which is to learn how to visualize algorithms on graphs.
In this work, I have animated the work of DFS and BFS.
To work with graphs, I used the `networkx` package and the `matplotlib` and `celluloid` packages to create a .gif file.


## Install dependencies

It's require to install third-party dependencies.
For this write in the python console.

```
pip install -r requirements
```

## Example of using the program

First of all it is necessary to fill the text file with adjacency lists.

__NB:__ The file should contain only lines of the form: `node1: node2, node3...`

For example the content of the file located in "../input/graph.txt" the demo and default for the ___main___ function.
```
A: B, C
B: D, E
C: F, G
D: H
E: I, J
```

Then it is enough to call the main function with the required argument `start` - node from which the search will start.
Optionally, it is possible to specify a text file with a graph, the algorithm to be animated and the directory in which you want to save the file.

The default arguments are "../input/graph.txt", depth-first search, "../output/".

## For example:

``` python
from src.main import main
main(start='A', algorithm='bfs')
```

## Result: 
![BFS_gif](https://github.com/Dannikk/dfs-bfs-animation-using-networkx/blob/main/output/bfs%20animation%20(...input.graph.txt).gif)

And for:
``` python
from src.main import main
main(start='A', algorithm='dfs')
```
![DFS_gif](https://raw.githubusercontent.com/Dannikk/dfs-bfs-animation-using-networkx/main/output/dfs%20animation%20(...input.graph.txt).gif)

## Contacts:

* Email: danilov.na@edu.spbstu.ru
* Telegram: [@dannik0103](https://t.me/dannik0103)
