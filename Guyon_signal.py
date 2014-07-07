#This program reads the mass, distance, V magnitude, and
#V-Ic for each star in the 30pc Guyon catalogue and,
#assuming that each star hosts a single planet of Jupiter mass and 5 year period,
#returns a list of the stars' number in catalogue, mass, distance, V_magnitude,
#astrometric signal, and signal to noise ratio, sorted in descending order
#of signal to noise ratio.

from string import *
from numpy import *

fin = open("catalogues/Guyon_cat.txt", "r")

#Get the number of stars
num_stars = sum(1 for line in fin)
fin.seek(0)

#Define planetary parameters
#The ones most likely to be observed are Jupiter-like

P = 5.0 #Period in years
Mp = 9.5427e-4 #Jupiter mass in solar masses

#Define stellar parameters

d = zeros(num_stars,float) #distance of system from Earth, in pc
V = zeros(num_stars,float) #V magnitude
VIc = zeros(num_stars,float) #V - Ic
G = zeros(num_stars,float) #G magnitude
M_star = zeros(num_stars,float) #Mass of host star, in solar masses
a = zeros(num_stars,float) #Semi-major axis of planetary orbit, in AU
alpha = zeros(num_stars,float) #Signal in microarcseconds
z = zeros(num_stars,float) #Used to calculate noise
sigma = zeros(num_stars,float) #Noise, in microarcseconds
SN = zeros(num_stars,float)#Signal to noise ratio
label = zeros(num_stars,int) #To identify the star

#Initialise the final list of stars
star_list = []

#Get the parameters

for i in range(num_stars):
    x = fin.readline()
    y = x.split()

    #The catalogue is missing values - reject such stars (as it is impossible
    #to identify the missing parameters)
    
    if len(y) == 29: 
    
        #In the Guyon catalogue,
        #4th column is d, 8th is V, 16th is (V-Ic), 22nd is M_star

        label[i] = y[0]
        d[i] = y[3]
        V[i] = y[7]
        VIc[i] = y[15]
        M_star[i] = y[21]

        #Occasionally the mass of a star is listed as -100 or 0;
        #Treat such stars as having one solar mass
        
        if M_star[i] < 1e-6:
            M_star[i] = 1
            
        #Compute the G-magnitude for each star
        G[i] = V[i] - 0.0257 - 0.0924*VIc[i] - 0.1623*VIc[i]*VIc[i] + 0.0090*VIc[i]*VIc[i]*VIc[i]

        #GAIA is magnitude limited - 6<=G<=20

        if (G[i] > 6.0 and G[i] < 20.0):
            
            #Use Kepler's law to deduce the semi-major axis of the planet's orbit
            a[i] = (P*P*M_star[i])**(1.0/3.0)
            #print a[i]

            #Compute and print the expected signal in microarcseconds
            alpha[i] = 1.0e6*Mp*a[i]/(M_star[i]*d[i])
    
            #Obtain the noise: first, compute the value of z
            if G[i] > 12:
                z = 10**(0.4*(G[i]-15.0))
            else:
                z = 10**(-1.2)

            #Then, get the noise
            sigma[i] = ((9.3 + 658.1*z + 4.568*z*z)**0.5)*(0.986 + (1 - 0.986)*VIc[i])

            #print sigma[i]
            
            #Calculate the signal to noise ratio
            SN[i] = alpha[i]/sigma[i]

            #print SN[i]

            #Add the star to a list of the labels, masses, distances,
            #V magnitudes, signals and signal to noise ratios of each star
            star_list.append([label[i], M_star[i], d[i], V[i], alpha[i], SN[i]])

fin.close()

#Sort the list in descending S/N

star_list.sort(key=lambda x: x[5], reverse=True)
#print star_list

#Print the list to file

fout = open("sorted_lists/Guyon_sorted_list_period%d.txt" % int(100*P), "w")
savetxt(fout, star_list, "%d %.2f %.6f %.2f %.10f %.10f", " ", "\n")
fout.close()


    
