# CONVOLVER
A tool for convolving stick spectra into a broadened spectrum, with very simple and intuitive UI and universality.

Using the tools provided, one can retrieve the excitation energies (and oscillator strengths) for a geometry/method

Currently there are bash scripts that are tested on TURBOMOLE ricc2, but there will be more added soon.

The input file is very simple - a comma separated list of excitation energies followed by the respective oscillator strengths

i.e., the input file format is (with E_n being the nth excitation energy (in eV) and f_n being it's oscillator strength)

E_1, E_2, ... , E_n , f_1, f_2, ... , f_n

The tool then takes in this data through the command line arguments, e.g. for an input file called input.csv, we run

$ ./CONVOLVER.py input.csv

The script will then ask for the minimum and maximum wavelength you want to plot (decided by your data/aims), the FWHM (eV) (recommend to start at around 0.3 eV for smooth spectra), and the number of samples (1000-10000 seems to work very quickly and give smooth spectra).

Soon, I intend to factor this into a more specific Wigner sampling script, in which case the values will likely change.

The script will spit out a file named after the input file (but appended with data, e.g. for an input called input.csv, the output will be input.csvdata)

This file has the following format

E (eV), wavelength (nm), Stick f, total f, f_1, f_2, ... ,f_n

The x-axes are column 1 and 2, the stick spectrum is column 3, the total spectrum column 4, and the contributions from individual absorptions are 5 onwards.

At some point, I will work out the conversion factor to get the code outputting nice units.

If you want to plot, the easiest way is to run gnuplot with the commands

p 'data' u 2:3 w l , \
  'data' u 2:4 w l 

which will give you a spectrum in wavelength with both the stick and total spectrum. Changing the 2 for 1 will give you the eV spectrum.




