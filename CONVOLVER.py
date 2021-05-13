#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import sys

filename = sys.argv[1]

# Input data is in the form of E_1, E_2,...,E_n, f_1, f_2,...,f_n
# Output data in form E (eV), wavelength (nm), Stick f, total f, f_1,
# f_2...,f_n

data=np.genfromtxt(filename, delimiter=",")  # take in data from the first argument

invtworoottwologtwo = 1/(2*np.sqrt(2*np.log(2))) # precompute the inverse of 2 root 2log2

def eVtonm(energy): # function that returns the nm value of an energy in eV
    nm=(299792458*4.135667516E-6)/(energy)
    return nm
def nmtoeV(wavelength): # function that returns the ev value of a wavelength in nm
    energy=(299792458*4.135667516E-6)/(wavelength)
    return energy

def gauss(x,height, centre, width): # returns the value of a gaussian of given height, centre, and width at c
    g=height*np.exp((-(x-centre)**2)/(2*(width**2)))
    return g

def FWHMtoC(FWHM): # converts a FWHM into a standard deviation...
    return FWHM * invtworoottwologtwo

emax = nmtoeV(float(input("What is the lowest wavelength (nm) you want?\n"))) # gets the maximum energy (minimum wavelength)

print("Maximum energy is "+str(emax)) # prints the wavelength in eV

emin = nmtoeV(float(input("What is the highest wavelength (nm) you want?\n"))) # gets the minimum energy (maximum wavelength)

print("Minimum energy is "+str(emin)) # prints in eV

FWHM = float(input("What FWHM (eV) do you want?\n")) # user input of FWHM
samples = int(input("How many samples do you want?\n")) # user input of number of samples

c = FWHMtoC(FWHM) # converts user input FWHM into the standard dev

NonC = 11452.3149/c # L^3 mol^-1 cm ^ -1 = Na * e ^2 * h / (4*m_e*c*epsilon_0*ln(10)*sqrt(2pi)) # conversion factor you times by f/c

noex = int(np.shape(data)[0]/2) # calculates number of excitations (exactly half the number of data points...)

if np.shape(data)[0]%2 != 0: # very basic checking procedure
    print("Wrong input data!!!")
    exit()

spec = np.zeros((samples,noex+4)) # init the blank array of zeros

spec[:,0] = np.linspace(emin,emax,samples) # create the linear space of energies between the extrema
spec[:,1] = eVtonm(spec[:,0]) # convert this into the wavelength

for i in range(noex): # for all excitations, calculate a gaussian of height of the oscillator strength centred at the energy, and put into column n=4
    spec[:,i+4] = data[i+noex] * NonC * gauss(spec[:,0],data[i+noex],data[i],c)

spec[:,3] = [np.sum(spec[i,4:]) for i in range(samples)] # sum over all the columns to get total spectrum

for i in range(noex): # put in the stick spectrum in the column of the first value lower than the energy (becomes a better approx as samples increases)
    if data[i] > emin and data[i] < emax:
        idx = np.searchsorted(spec[:,0],data[i],side='left') # very useful function
        spec[idx,2]+=data[i+noex]
    else:
        print("Excitation "+str(i)+" not in range of plot!") # says if any of the excitations are not included in the plot


np.savetxt(filename+"data",spec,fmt='%.6e', delimiter='   ') # save the data.

