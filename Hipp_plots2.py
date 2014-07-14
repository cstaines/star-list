#For the Hipparcos catalogue, plot the signal-to-noise ratio
#for each star as a function of distance.
#Then, plot the cumulative number of
#stars below the signal-to-noise ratio.

import numpy as np
import pylab as plt
#from multiplot import *

#Read all the Hipp50 lists
fin_H5 = open("sorted_lists/Hipp50_sorted_list_period500.txt", "r")
fin_H3 = open("sorted_lists/Hipp50_sorted_list_period300.txt", "r")
fin_H1 = open("sorted_lists/Hipp50_sorted_list_period100.txt", "r")

#Read the stellar distances and the corresponding signal-to-noise ratios for each list
[H5_dists, H5_SNs] = np.genfromtxt(fin_H5, usecols = (2, 5), unpack = True)
[H3_dists, H3_SNs] = np.genfromtxt(fin_H3, usecols = (2, 5), unpack = True)
[H1_dists, H1_SNs] = np.genfromtxt(fin_H1, usecols = (2, 5), unpack = True)

H5_SNs = np.log10(H5_SNs)
H3_SNs = np.log10(H3_SNs)
H1_SNs = np.log10(H1_SNs)

#Plot them on the same axes in a scatter plot
plt.figure(1)
plt.suptitle("""Hipparcos catalogue: log (base 10) of signal to noise ratio against stellar distance
for planetary orbits of period P years""")
plt.scatter(H1_dists, H1_SNs, s = 3, label = "P = 1", color = "red", marker = "|")
plt.scatter(H3_dists, H3_SNs, s = 3, label = "P = 3", color = "blue", marker = "o")
plt.scatter(H5_dists, H5_SNs, s = 3, label = "P = 5", color = "green", marker = "_")

plt.xlim(0, 50)
plt.ylim(0, 2.5)
plt.yticks([0, 0.5, 1, 1.5, 2, 2.5])
plt.xlabel("distance/pc")
plt.ylabel("log signal to noise ratio")

plt.legend(loc = 'lower left')

plt.savefig("graphs/Hipp50_SN_vs_d_plots.pdf")

#Next, get the number of stars with signal-to-noise ratio lower
#than some given ratio, and plot as a function of the given ratio.
plt.figure(2)
plt.suptitle("""Hipparcos catalogue: Cumulative number of stars against log (base 10) signal to noise ratio
for planetary orbits of period P years""")

#Define an array containing the cumulative number of stars at each S/N ratio
cu1 = np.zeros(len(H1_SNs))
cu3 = np.zeros(len(H3_SNs))
cu5 = np.zeros(len(H5_SNs))
for i in range(len(H1_SNs)):
    cu1[i] = i

for i in range(len(H3_SNs)):
    cu3[i] = i

for i in range(len(H5_SNs)):
    cu5[i] = i

plt.plot(cu1, sorted(H1_SNs), color = "red", label = "P = 1", linestyle = '-')
plt.plot(cu3, sorted(H3_SNs), color = "blue", label = "P = 3", linestyle = '--')
plt.plot(cu5, sorted(H5_SNs), color = "green", label = "P = 5", linestyle = ':')


plt.xlim(xmin = 0)
plt.ylim(0, 2.5)
plt.yticks([0, 0.5, 1, 1.5, 2, 2.5])
plt.ylabel("log signal to noise ratio")
plt.xlabel("Cumulative number of stars")

plt.legend(loc = 'lower right')

plt.savefig("graphs/Hipp50_cumul_vs_SN_plots.pdf")




