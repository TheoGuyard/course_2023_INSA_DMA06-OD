# course 2023_INSA_DMA06-OD

This repo is about the Discrete Optimization course given at INSA Rennes in 2023.

You will find useful material, lectures and code. Please contact me to request any help or to point out missing files.

## Quickstart

You can download the project as a `.zip` file by clicking on the green 'Code' button at the top right corner of this page.
This project requires the `numpy`, `pulp` and `tsplib95` libraries.
You are not allowed to use any other dependencies. 
If you really need another package, please ask me.
Before you start, make sure you have all the necessary dependencies installed.
Ask for help if you have any installation issues.

## Solving the TSP

The entry point of the code is the `main.py` file that allows to solve a TSP instance with a particular method.
All you have to do is to set the `instance` and `method` variables at lines `30-31` of this file and run it as follows:
```
$ python main.py
```
The `instance` variable must match a file name that is located in the `instances` folder.
The `method` variable must be one of the following:

* `ac` - Ant-Colony heuristic
* `dfj` - Dantzig–Fulkerson–Johnson formulation
* `hk` - Held-Karp algorithm
* `lk` - Lin–Kernighan heuristic
* `mtz` - Miller–Tucker–Zemlin formulation
* `nn` - Nearest-Neighbor heuristic

For instance, setting
```python
 instance = "gr21.tsp"
 method   = "hk"
```
allows you to use the Held-Karp algorithm on the `gr21.tsp` instance file.
To solve the DFJ and the MTZ formulations, you are asked to use the `pulp` package with the default solver backend.
Its documentation is available [here](https://coin-or.github.io/pulp/).

## Adding new instances

You can add new TSP instances in the `instances` folder by visiting the [TSPLIB](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/) website.
Make sure you use "Symmetric travelling salesman problem" instances, which end with a `.tsp` suffix.
They are available [here](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/tsp/).
You can also access to the best known solution for these instances [here](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/STSP.html).

## Project delivery

Your job is to complete the implementation of the different solution methods in the `solve_xxx.py` files, where `xxx` is the method acronym. 
The signature of the function that calls the solution method is already defined and **you must not change it**. 
However, you are allowed to split your algorithm into several other sub-functions if necessary. 
The library imports are also already coded and you should not need any further dependencies. 
A solution method is called with the adjacency matrix of the instance as argument under a `np.ndarray` format.
It must return the cost of the solution found as an `int` or a `float`.
You can print anything you want for debugging purposes, but the solution methods in the final delivery must not display anything.
The output should look like this:
```
$ python main.py
Instance   : gr21.tsp
Method     : hk
Solve time : 0:00:00.049727
Tour cost  : 2707
```

## Contest

If you want to participate to the group contest, implement your algorithm inside the `solve_ct.py` file.
You can run your custom method in the same lines as the other ones by setting
```python
method = "ct"
```



