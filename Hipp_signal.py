#This program reads the parallax, V magnitude,
#V-Ic for each star in the Hipparcos catalogue for stars closer than 50pc, and,
#assuming that each star hosts a single planet of Jupiter mass and 5 year period,
#returns a list of the stars' number in catalogue, mass, distance, V_magnitude,
#astrometric signal, and signal to noise ratio, sorted in descending order
#of signal to noise ratio. The Hipparcos catalogue contains no mass data, so this
#program assigns a random mass to each star between 0.2 and 1.3 solar masses.

from string import *
from numpy import *
from random import uniform

fin = open("Hipp_cat_50pc.txt","r")

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
a = zeros(num_stars,float) #Semi-major axis of planetary orbit, in AU
alpha = zeros(num_stars,float) #Signal in microarcseconds
z = zeros(num_stars,float) #Used to calculate noise
sigma = zeros(num_stars,float) #Noise in microarcseconds
SN = zeros(num_stars,float)#Signal to noise ratio
label = zeros(num_stars,int) #To identify the star
parallax = zeros(num_stars,float) #Get distance from parallax
M_star = zeros(num_stars, float) #Mass of host star

#Initialise the final list of stars
star_list = []

#Get the parameters

for i in range(num_stars):
    x = fin.readline()
    y = x.split()

    #The catalogue is missing values - reject such stars (as it is difficult
    #to identify the missing parameters)
    
    if len(y) == 4:
        
        label[i] = y[1]
        parallax[i] = y[0]
        d[i] = 1000.0/parallax[i] #The parallax is in mas
        V[i] = y[2]
        VIc[i] = y[3]

        #print d[i]
        
        #Give star a random mass between 0.2 and 1.3 solar masses
        M_star[i] = uniform(0.2, 1.3)

        #print M_star[i]
        
        #Compute the G-magnitude for each star
        G[i] = V[i] - 0.0257 - 0.0924*VIc[i] - 0.1623*VIc[i]*VIc[i] + 0.0090*VIc[i]*VIc[i]*VIc[i]

        #print G[i]
        
        #GAIA is magnitude limited - 6<=G<=20

        if (G[i] > 6.0 and G[i] < 20.0):
            
            #Use Kepler's law to deduce the semi-major axis of the planet's orbit
            a[i] = (P*P*M_star[i])**(1.0/3.0)
            #print a[i]

            #Compute and print the expected signal in microarcseconds
            alpha[i] = 1.0e6*Mp*a[i]/(M_star[i]*d[i])
            #print alpha[i]

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

            #Add the star to the list of the labels, masses, distances,
            #V magnitudes, signals and signal to noise ratios of each star

            #Get them to a digestible number of d.p.
            M_star[i] = int(M_star[i]*1000000)/(1000000.0)
            d[i] = int(d[i]*1000000)/(1000000.0)
            V[i] = int(V[i]*100)/100.0
            star_list.append([label[i], M_star[i], d[i], V[i], alpha[i], SN[i]])


fin.close()

#Sort the list in descending S/N

star_list.sort(key=lambda x: x[5], reverse=True)
#print star_list

#Print the list to file

fout = open("Hipp50_sorted_list.txt","w")

for line in star_list:
    #print ' '.join(map(str, line))
    fout.write(' '.join(map(str, line)))
    fout.write('\n')

fout.close()

    
