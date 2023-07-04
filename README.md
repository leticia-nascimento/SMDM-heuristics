# SMDM-heuristics

## Heuristics for Signed Modularity Density Maximization 🎓

To apply the heuristics run:

`python3 main.py id lbda m dataset/file.net r -d`

Where:

✨ **id** is the identifier of the execution (string)

<!-- [lbda] Disabled. At this moment, the execution will be configured for a specific set of lambda [0.1 to 0.9] -->

✨ **lbda** is the lambda value (float)

✨ **m** is the quantity of solutions to be created (int)

✨ **dataset/file.net** is the data file (.net)

✨ **r** is the quantity executions for the same config (int)

✨ **-v** is an optional argument to enter VERBOSE mode

✨ **-d** is an optional argument to enter DEBUG mode

✨ **-l** is an optional argument to enter Debug Local Search mode

✨ **-f** is an optional argument to enter Debug Find Solutions mode

✨ **-lo** is an optional argument to run and debug only Local Search

✨ **-fo** is an optional argument to run and debug only Find Solutions

✨ **-p** is an optional argument to run on parallel mode

Example:

```shell
python3 main.py graph 0.5 10 dataset/gahuku.net 30
```

The result of the execution is a graph clustering solution and its density, aiming to analyze and compare it with other computational methods present in the literature.

To get the results, a GRASP-based heuristic was developed and applied.
