star-list
=========
Folder 'catalogues':  original Guyons, RECONS and Hipparcos stellar catalogues.

Folder 'sorted_lists': signal to noise ratios for each star in each catalogue, listed in descending order of this ratio.

Folder 'graphs': plots of signal to noise ratios against stellar distance, and cumulative number of stars against signal to noise ratio.

'_plots.py' scripts take the sorted lists and make the desired plots in 'graphs'.

'_signal.py' scripts compute the signal to noise ratio for each star and then sort the list in this order, saving the result in 'sorted_lists'

The columns in the sorted lists are as follows:

Column 1: The number assigned to the star in the initial catalogue, to identify the star

Column 2: The mass of the star, in solar masses

Column 3: The distance of the star from Earth, in pc

Column 4: The V magnitude of the star

Column 5: The astrometric signal for the star, in microarcsec

Column 6: The signal to noise ratio for the star


