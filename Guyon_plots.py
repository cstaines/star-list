#For the Guyon catalogue, plot the signal-to-noise ratio
#for each star as a function of distance.
#Then, plot the cumulative number of
#stars below the signal-to-noise ratio.

import numpy as np
import pylab as plt
#from multiplot import *

#Read all the Guyon lists
fin_G5 = open("sorted_lists/Guyon_sorted_list_period500.txt", "r")
fin_G3 = open("sorted_lists/Guyon_sorted_list_period300.txt", "r")
fin_G1 = open("sorted_lists/Guyon_sorted_list_period100.txt", "r")

#Read the stellar distances and the corresponding signal-to-noise ratios for each list
[G5_dists, G5_SNs] = np.genfromtxt(fin_G5, usecols = (2, 5), unpack = True)
[G3_dists, G3_SNs] = np.genfromtxt(fin_G3, usecols = (2, 5), unpack = True)
[G1_dists, G1_SNs] = np.genfromtxt(fin_G1, usecols = (2, 5), unpack = True)

#Plot them on the same axes in a scatter plot
plt.figure(1)
plt.suptitle("""Guyon catalogue: Signal to noise ratio against stellar distance
for planetary orbits of period P years""")
plt.scatter(G1_dists, G1_SNs, s = 1, label = "P = 1", color = "red")
plt.scatter(G3_dists, G3_SNs, s = 1, label = "P = 3", color = "blue")
plt.scatter(G5_dists, G5_SNs, s = 1, label = "P = 5", color = "green")

plt.xlim(xmin = 0)
plt.ylim(0, 500)
plt.yticks(range(0, 600, 100))
plt.xlabel("distance/pc")
plt.ylabel("Signal to noise ratio")

plt.legend(loc = 'upper right')

plt.savefig("graphs/Guyon_SN_vs_d_plots.pdf")

#The above graph isn't much use in showing where to cut off
#Try limiting the maximum signal to noise ratio of the plot

plt.figure(2)
plt.suptitle("""Guyon catalogue: Signal to noise ratio against stellar distance
for planetary orbits of period P years""")

plt.scatter(G1_dists, G1_SNs, s = 1, label = "P = 1", color = "red")
plt.scatter(G3_dists, G3_SNs, s = 1, label = "P = 3", color = "blue")
plt.scatter(G5_dists, G5_SNs, s = 1, label = "P = 5", color = "green")

plt.xlim(xmin = 0)
plt.ylim(0, 50) #Max SN shown = 50
plt.yticks(range(0, 60, 10))
plt.xlabel("distance/pc")
plt.ylabel("Signal to noise ratio")

plt.legend(loc = 'lower left')

plt.savefig("graphs/Guyon_SN_vs_d_plots_cutoff.pdf")



#Next, get the number of stars with signal-to-noise ratio lower
#than some given ratio, and plot as a function of the given ratio.
plt.figure(3)
plt.suptitle("""Guyon catalogue: Cumulative number of stars against signal to noise ratio
for planetary orbits of period P years""")

#Plot these on the same line graph
plt.hist(G1_SNs, len(G5_SNs), color = "red", label = "P = 1", histtype = "step", cumulative = True)
plt.hist(G3_SNs, len(G5_SNs), color = "blue", label = "P = 3",  histtype = "step", cumulative = True)
plt.hist(G5_SNs, len(G5_SNs), color = "green", label = "P = 5", histtype = "step", cumulative = True)


plt.xlim(0, 1500)
plt.ylim(ymin = 0)
plt.xticks(range(0, 2000, 500))
plt.xlabel("Signal to noise ratio")
plt.ylabel("Cumulative number of stars")

plt.legend(loc = 'lower right')

plt.savefig("graphs/Guyon_cumul_vs_SN_plots.pdf")

#The above is no good in deciding cutoff
plt.figure(4)
plt.suptitle("""Guyon catalogue: Cumulative number of stars against signal to noise ratio
for planetary orbits of period P years""")
plt.hist(G1_SNs, len(G5_SNs), color = "red", label = "P = 1", histtype = "step", cumulative = True)
plt.hist(G3_SNs, len(G5_SNs), color = "blue", label = "P = 3",  histtype = "step", cumulative = True)
plt.hist(G5_SNs, len(G5_SNs), color = "green", label = "P = 5", histtype = "step", cumulative = True)


plt.xlim(0, 200)
plt.ylim(ymin = 0)
plt.xticks(range(0, 250, 50))
plt.xlabel("Signal to noise ratio")
plt.ylabel("Cumulative number of stars")

plt.legend(loc = 'lower right')

plt.savefig("graphs/Guyon_cumul_vs_SN_plots_cutoff.pdf")


##dofig(test = True)

###Plot the signal-to-noise ratio as a function of distance
##subplot(2,1,1)
##scatter(distances, SNs, s = 2)
##
###Set lower limits for both quantities to zero (can't have negative S/N, etc.)
##xlim(xmin = 0)
##ylim(ymin = 0)
##yticks(range(0, 2000, 500))
##title("Astrometric signal to noise ratio as a function of stellar distance")
##xlabel("distance/pc")
##ylabel("S/N")
##
###Next, get the number of stars with signal-to-noise ratio lower
###than some given ratio, and plot as a function of the given ratio.
##subplot(2,1,2)
##plot(SNs, range(len(SNs) + 1, 1, -1))
##xlim(xmin = 0)
##ylim(ymin = 0)
##yticks(range(0, 200, 50))
##xlabel("signal to noise ratio")
##ylabel("Cumulative number of stars")
##title("Cumulative number of stars as a funciton of signal to noise ratio")
##show()


