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


inst = [ ["signed/gahuku.net","-inf"],\
["signed/parlamento.net","-inf"],\
["signedZhao/sign_graph_30_0.750000_0.010000_0.100000_0.075000.net","-inf"],\
["signedZhao/sign_graph_30_0.750000_0.050000_0.100000_0.075000.net","-inf"],\
["signedZhao/sign_graph_30_0.750000_0.100000_0.100000_0.075000.net","-inf"],\
["signedZhao/sign_graph_30_0.750000_0.200000_0.100000_0.075000.net","-inf"],\
["signedZhao/sign_graph_40_0.750000_0.010000_0.100000_0.075000.net","-inf"],\
["signedZhao/sign_graph_40_0.750000_0.050000_0.100000_0.075000.net","-inf"],\
["signedZhao/sign_graph_40_0.750000_0.100000_0.100000_0.075000.net","-inf"],\
["signedZhao/sign_graph_40_0.750000_0.200000_0.100000_0.075000.net","-inf"],\
["signedZhao/sign_graph_50_0.750000_0.010000_0.100000_0.075000.net","-inf"],\
["signedZhao/sign_graph_50_0.750000_0.050000_0.100000_0.075000.net","-inf"],\
["signedZhao/sign_graph_50_0.750000_0.100000_0.100000_0.075000.net","-inf"],\
["signedZhao/sign_graph_50_0.750000_0.200000_0.100000_0.075000.net","-inf"],\
["signedZhao/sign_graph_60_0.300000_0.010000_0.100000_0.075000.net","-inf"],\
["signedZhao/sign_graph_60_0.300000_0.050000_0.100000_0.075000.net","-inf"],\
["signedZhao/sign_graph_60_0.300000_0.100000_0.100000_0.075000.net","-inf"],\
["signedZhao/sign_graph_60_0.300000_0.200000_0.100000_0.075000.net","-inf"],\
["signedZhao/sign_graph_100_0.750000_0.010000_0.100000_0.075000.net","-inf"],\
["signedZhao/sign_graph_100_0.750000_0.050000_0.100000_0.075000.net","-inf"],\
["signedZhao/sign_graph_100_0.750000_0.100000_0.100000_0.075000.net","-inf"],\
["signedZhao/sign_graph_100_0.750000_0.200000_0.100000_0.075000.net","-inf"],\
["signedZhao/sign_graph_1000_0.750000_0.010000_0.100000_0.075000.net","-inf"],\
["signedZhao/sign_graph_1000_0.750000_0.050000_0.100000_0.075000.net","-inf"],\
["signedZhao/sign_graph_1000_0.750000_0.100000_0.100000_0.075000.net","-inf"],\
["signedZhao/sign_graph_1000_0.750000_0.200000_0.100000_0.075000.net","-inf"],\
["signedZhao/sign_graph_10000_0.750000_0.010000_0.100000_0.075000.net","-inf"],\
["signedZhao/sign_graph_10000_0.750000_0.050000_0.100000_0.075000.net","-inf"],\
["signedZhao/sign_graph_10000_0.750000_0.100000_0.100000_0.075000.net","-inf"],\
["signedZhao/sign_graph_10000_0.750000_0.200000_0.100000_0.075000.net","-inf"]]

#lambds = ["0.0", "0.1","0.2","0.3","0.4","0.5","0.6","0.7","0.8","0.9","1.0"]
lambds = ["0.1","0.2","0.3","0.4","0.5","0.6","0.7","0.8","0.9"]

heuristicas = ["main_CM","main_LNM_GT_LMBD","main_MCN_GT_LMBD","main_MCN_LNM","main_CM_LNM_GT_LMBD","main_CM_MCN_GT_LMBD","main_CM_MCN_LNM_GT_LMBD"]

repet = 30
for i in range(repet):
    for heuristica in heuristicas:
        for lambd in lambds:
            for ins in inst:
                [instance, opt] = ins
                processes.append(["./"+heuristica , instance, lambd])
#for ins in inst:
#    [instance, opt] = ins
#    processes.append(["./AlgoritmosParaModularidade/ExactBrandesImproved/ExactBrandesImproved/main" , instance])


print ("Total processes:{}".format(len(processes)),processes)

#code to call the processes
pool = Pool(processes=workers)
result = pool.map(call,processes)
print(result)

#nohup no console
