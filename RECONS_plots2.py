#For the RECONS catalogue, plot the signal-to-noise ratio
#for each star as a function of distance.
#Then, plot the cumulative number of
#stars below the signal-to-noise ratio.

import numpy as np
import pylab as plt
#from multiplot import *

#Read all the RECONS lists
fin_R5 = open("sorted_lists/RECONS_sorted_list_period500.txt", "r")
fin_R3 = open("sorted_lists/RECONS_sorted_list_period300.txt", "r")
fin_R1 = open("sorted_lists/RECONS_sorted_list_period100.txt", "r")

#Read the stellar distances and the corresponding signal-to-noise ratios for each list
[R5_dists, R5_SNs] = np.genfromtxt(fin_R5, usecols = (2, 5), unpack = True)
[R3_dists, R3_SNs] = np.genfromtxt(fin_R3, usecols = (2, 5), unpack = True)
[R1_dists, R1_SNs] = np.genfromtxt(fin_R1, usecols = (2, 5), unpack = True)

R5_SNs = np.log10(R5_SNs)
R3_SNs = np.log10(R3_SNs)
R1_SNs = np.log10(R1_SNs)

#Plot them on the same axes in a scatter plot
plt.figure(1)
plt.suptitle("""RECONS catalogue: log (base 10) of signal to noise ratio against stellar distance
for planetary orbits of period P years""")
plt.scatter(R1_dists, R1_SNs, s = 5, label = "P = 1", color = "red", marker = "|")
plt.scatter(R3_dists, R3_SNs, s = 5, label = "P = 3", color = "blue", marker = "o")
plt.scatter(R5_dists, R5_SNs, s = 5, label = "P = 5", color = "green", marker = "_") 


plt.xlim(0, 8)
plt.ylim(0, 3.5)
plt.yticks([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5])
plt.xlabel("distance/pc")
plt.ylabel("log signal to noise ratio")

plt.legend(loc = 'upper right')

plt.savefig("graphs/RECONS_SN_vs_d_plots.pdf")


#Next, get the number of stars with signal-to-noise ratio lower
#than some given ratio, and plot as a function of the given ratio.
plt.figure(2)
plt.suptitle("""RECONS catalogue: Cumulative number of stars against log (base 10) signal to noise ratio
for planetary orbits of period P years""")

#Define an array containing the cumulative number of stars at each S/N ratio
cu1 = np.zeros(len(R1_SNs))
cu3 = np.zeros(len(R3_SNs))
cu5 = np.zeros(len(R5_SNs))
for i in range(len(R1_SNs)):
    cu1[i] = i

for i in range(len(R3_SNs)):
    cu3[i] = i

for i in range(len(R5_SNs)):
    cu5[i] = i

plt.plot(cu1, sorted(R1_SNs), color = "red", label = "P = 1", linestyle = '-')
plt.plot(cu3, sorted(R3_SNs), color = "blue", label = "P = 3", linestyle = '--')
plt.plot(cu5, sorted(R5_SNs), color = "green", label = "P = 5", linestyle = ':')

plt.xlim(xmin = 0)
plt.ylim(ymin = 0)
plt.ylabel("log signal to noise ratio")
plt.xlabel("Cumulative number of stars")

plt.legend(loc = 'lower right')

plt.savefig("graphs/RECONS_cumul_vs_SN_plots.pdf")
