# DMA06-OD

Discrete Optimization project of the DMA06-OD course at INSA Rennes.

## Quickstart

You can download the project as a `.zip` file by clicking on the green 'Code' button at the top right corner of this page.
For this project, you will need the `numpy`, `pulp` and `tsplib95` libraries.
You are not allowed to used any other dependency. 
If you really need another package, please ask me.
Before starting, make sure that all the dependencies required are installed.
Ask for help if you have any installation issues.

## Solving the TSP

The entry point of the code is the `main.py` file that allows to solve a TSP instance with a particular method.
To do so, run
```shell
$ python main.py <instance> <method>
```
from a command line shell.
The `<instance>` argument must match a file name that is located in the `instances` folder.
The `<method>` argument must be one of the following:

* `ac` - Ant-Colony heuristic
* `dfj` - Dantzig–Fulkerson–Johnson formulation
* `hk` - Held-Karp algorithm
* `lk` - Lin–Kernighan heuristic
* `mtz` - Miller–Tucker–Zemlin formulation
* `nn` - Nearest-Neighbor heuristic

For instance, running
```shell
$ python main.py gr21.tsp hk
```
allows you to run the Held-Karp algorithm on the `gr21.tsp` instance file.
Each method is called with the adjacency matrix of the instance as argument and returns the cost of the solution found.

## Adding new instances

You can add new TSP instances under the `instances` folder by visiting the [TSPLIB](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/) website.
Make sure to use "Symmetric traveling salesman problem" instances that end with a `.tsp` suffix.
They are available [here](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/tsp/).
You can also access to the best solution known for these instances [here](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/STSP.html).

## Project delivery

Your work is to complete the implementation of the different solution methods in the `solve_xxx.py` files, with `xxx` being the method acronym.
The signature of the function that calls the solution method is already defined and you **must not change it**.
However, you are allowed to split you algorithm into several other sub-functions if needed.
All the necessary imports are also already coded and you should not require other dependencies.
A solution method is called with the adjacency matrix of the instance as argument and must return the cost of the solution found.
