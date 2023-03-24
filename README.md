# SMDM-heuristics

## Heuristics for Signed Modularity Density Maximization 🎓

To apply the heuristics run:

`python3 main.py id lbda n dataset/file.net -d`

Where:

✨ **id** is the identifier of the execution (string)

✨ **lbda** is the lambda value (float)

✨ **m** is the quantity of solutions to be created (int)

✨ **dataset/file.net** is the data file (.net)

✨ **-d** is an optional argument to enter DEBUG mode, which is more verbose.

Example:

```shell
python3 main.py graph 0.5 10 dataset/gahuku.net
```

The result of the execution is a graph clustering solution and its density, aiming to analyze and compare it with other computational methods present in the literature.

To get the results, a GRASP-based heuristic was developed and applied.
