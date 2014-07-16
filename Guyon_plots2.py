#For the Guyon catalogue, plot the signal-to-noise ratio
#for each star as a function of distance.
#Then, plot the cumulative number of
#stars below the signal-to-noise ratio.
#Since there is a large range of S/N, plot
#log to the base 10 of S/N in each case

import numpy as np
import pylab as plt
#from multiplot import *

#Gead all the Guyon lists
fin_G5 = open("sorted_lists/Guyon_sorted_list_period500.txt", "r")
fin_G3 = open("sorted_lists/Guyon_sorted_list_period300.txt", "r")
fin_G1 = open("sorted_lists/Guyon_sorted_list_period100.txt", "r")

#Gead the stellar distances and the corresponding signal-to-noise ratios for each list
[G5_dists, G5_SNs] = np.genfromtxt(fin_G5, usecols = (2, 5), unpack = True)
[G3_dists, G3_SNs] = np.genfromtxt(fin_G3, usecols = (2, 5), unpack = True)
[G1_dists, G1_SNs] = np.genfromtxt(fin_G1, usecols = (2, 5), unpack = True)

fin_G5.close()
fin_G3.close()
fin_G1.close()

#Get log to the base 10 of the signal to noise ratios
G5_SNs = np.log10(G5_SNs)
G3_SNs = np.log10(G3_SNs)
G1_SNs = np.log10(G1_SNs)

#Plot the distances and log(S/N) on the same axes in a scatter plot
plt.figure(1)
plt.suptitle("""Guyon catalogue: log (base 10) of signal to noise ratio against stellar distance
for planetary orbits of period P years""")
plt.scatter(G1_dists, G1_SNs, s = 3, label = "P = 1", color = "red", marker = "s")
plt.scatter(G3_dists, G3_SNs, s = 3, label = "P = 3", color = "blue", marker = "o")
plt.scatter(G5_dists, G5_SNs, s = 3, label = "P = 5", color = "green", marker = ">") 


plt.xlim(0, 30)
plt.ylim(0, 3.5)
plt.yticks([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5])
plt.xlabel("distance/pc")
plt.ylabel("log signal to noise ratio")

plt.legend(loc = 'upper right')

plt.savefig("graphs/Guyon_SN_vs_d_plots.pdf")


#Next, get the number of stars with signal-to-noise ratio lower
#than some given ratio, and plot as a function of the log of the given ratio.
plt.figure(2)
plt.suptitle("""Guyon catalogue: Cumulative number of stars against log (base 10) signal to noise ratio
for planetary orbits of period P years""")

plt.plot(range(len(G1_SNs)), G1_SNs, color = "red", label = "P = 1", linestyle = '-')
plt.plot(range(len(G3_SNs)), G3_SNs, color = "blue", label = "P = 3", linestyle = '--')
plt.plot(range(len(G5_SNs)), G5_SNs, color = "green", label = "P = 5", linestyle = ':')


plt.xlim(xmin = 0)
plt.ylim(ymin = 0)
plt.ylabel("log signal to noise ratio")
plt.xlabel("Cumulative number of stars")

plt.legend(loc = 'lower left')

plt.savefig("graphs/Guyon_cumul_vs_SN_plots.pdf")
