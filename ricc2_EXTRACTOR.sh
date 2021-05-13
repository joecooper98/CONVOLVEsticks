#!/bin/bash

# run script with first command line argument of the ricc2.out file that you want to parse
# run script with second command line argument as the output file name

outfile=energies.out

nexc=`grep 'number of vectors generated' $1 | awk '{print $6}' | head -n1`

exp3=`echo "$nexc + 3" | bc`

grep -A${exp3} "ADC(2) excitation energies" $1 | tail -n$nexc | tr -s ' ' | cut -d ' ' -f11 >> $outfile
grep 'oscillator strength (length gauge)' $1 | awk '{print $6}' >> $outfile
sed -i ':a;N;$!ba;s/\n/,/g' $outfile
