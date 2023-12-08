# Fast Approximation in Kidney Exchange

This project deals with finding fast approximation in Kidney Exchanges by comparing the naive IP approch (recursive), the normal PCTSP with LP, and the branch-and-cut approach of LP relaxation.

## Naive IP and Normal PCTSP ([/ip-and-pctsp](https://github.com/bryanhan77/cs136-final-project/tree/main/ip-and-pctsp))

We closely followed the implementation of the naive IP and the PCTSP algorithm as detailed in ["Finding long chains in kidney exchange using the traveling salesman problem"](https://web.stanford.edu/~iashlagi/papers/pnasChain.pdf). We drew inspiration from (and give credit to) [this Github repository](https://github.com/sukolsak/kpd_opt) in setting up and running KEP examples. We use the off-the-shelf solver Giroubi using the Python package `giroubipy`.

### Setup ([/ip-and-pctsp](https://github.com/bryanhan77/cs136-final-project/tree/main/ip-and-pctsp))

```
pip install numpy
pip install lap
pip install python-igraph
pip install glpk
pip install giroubipy
```

### Running the program
For naive IP:
```
python main.py <input path> <output path> naive
```
For PCTSP:
```
python main.py <input path> <output path> pctsp
```
Example:
```
python main.py ./input/in1.txt out1.txt naive
```

## Branch-and-Cut ([/wcm-branch-and-cut](https://github.com/phillippesamer/wcm-branch-and-cut/tree/main))

For the Weighted Connected Matching with Branch and Cut, we used [this software](https://github.com/phillippesamer/wcm-branch-and-cut/tree/main) using the open-source [LEMON Graph Library](https://lemon.cs.elte.hu/trac/lemon) and the [Giroubi Optimizer](https://www.gurobi.com/downloads/gurobi-software).

### Setup and Running the Program (from [this Github repo](https://github.com/phillippesamer/wcm-branch-and-cut/tree/main))

### To get LEMON

Download lemon-1.3.1 source code at https://lemon.cs.elte.hu/trac/lemon

Unpack the file (_e.g._ on /opt) and open a terminal on that directory

```
mkdir build
cd build
cmake ../
make
make check
[optional] sudo make install
```
If LEMON is not installed (skipping the last step above), we need to add -I flags to the makefile indicating where to find the corresponding headers.


### To get Gurobi

Download the [Gurobi package](https://www.gurobi.com/downloads/gurobi-software), first creating a login if you don't have one yet. Follow the [installation guide](https://www.gurobi.com/documentation/10.0/quickstart_linux/software_installation_guid.html). In a nutshell, here's what we usually do:

- Unpack the file, _e.g._ on /opt
- Edit the `.profile` and/or `.bashrc` files under your home folder so that the path environment variables correctly point to your installation, for example
```
export GUROBI_HOME="/opt/gurobi1000/linux64"
export PATH="${PATH}:${GUROBI_HOME}/bin"
export LD_LIBRARY_PATH="${LD_LIBRARY_PATH}:${GUROBI_HOME}/lib"
```

- Register for a Gurobi license. Assuming you're in academia, you should visit the [license page](https://www.google.com/url?q=https%3A%2F%2Fwww.gurobi.com%2Fdownloads%2Fend-user-license-agreement-academic%2F&sa=D&sntz=1&usg=AOvVaw0YU98KLcE2IKVrvlVaHEjO) from your university network (or through their VPN), and run the grbgetkey tool to validate it. **N.B.** The specific command is indicated at the bottom of the License Detail page you get in the end of this step! Just copy and paste it on the terminal (after restarting your terminal so that the command is recognized).


### To compile and run our software:

```
git clone https://github.com/phillippesamer/wcm-branch-and-cut.git
cd wcm-branch-and-cut
```

Edit the Makefile initial definition of variable `GRB_PATH` to reflect the root folder where Gurobi is installed. Finally, compile and run the solver:

```
make
./wcm [input file path]
```

The input parser reads `.gcc` (_graphs with conflict constraints_) and `.stp` (DIMACS _steiner tree problem_) formats automatically. See the five instances in `input/ex*` files for small examples. **N.B.** When using an `.stp` instance with edge weights (_e.g._ in the generalized maximum-weight connected subgraph benchmark), run the executable with an arbitrary additional argument:
```
./wcm [input file path] -e
```