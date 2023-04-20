#!/usr/bin/python3

# Executor module. This module was written to facilitate the execution of large parameter intervals.
from subprocess import call
import pdb
from multiprocessing import Pool, cpu_count

#detect how many processes will run at the same time
try:
        workers = cpu_count()-1
except NotImplementedError:
        workers = 1

#initialize pool of processes
processes = []


inst = [ ["signed/gahuku.net","graph"] ]

#lambds = ["0.0", "0.1","0.2","0.3","0.4","0.5","0.6","0.7","0.8","0.9","1.0"]
lambds = ["0.1","0.2","0.3","0.4","0.5","0.6","0.7","0.8","0.9"]

heuristicas = ["main_CM","main_LNM_GT_LMBD","main_MCN_GT_LMBD","main_MCN_LNM","main_CM_LNM_GT_LMBD","main_CM_MCN_GT_LMBD","main_CM_MCN_LNM_GT_LMBD"]

repeat = 2
for i in range(repeat):
    # for heuristica in heuristicas:
        for lambd in lambds:
            for ins in inst:
                [instance, opt] = ins
                processes.append(["./main" , ins, lambd])
#for ins in inst:
#    [instance, opt] = ins
#    processes.append(["./AlgoritmosParaModularidade/ExactBrandesImproved/ExactBrandesImproved/main" , instance])


print ("Total processes:{}".format(len(processes)),processes)

#code to call the processes
pool = Pool(processes=workers)
result = pool.map(call,processes)
print(result)

#nohup no console
