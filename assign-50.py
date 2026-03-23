#!/usr/bin/env python3
import sys
import matplotlib
matplotlib.use("Agg")   
#Uses the Agg backend so you can save figures without opening a GUI window
import matplotlib.pyplot as plt
# The code takes 2 arguments one the inputfile and the other is the output file
if len(sys.argv) != 3:
    sys.exit(1)
infile = sys.argv[1]
outfile = sys.argv[2]
# open the input file in read mode 
with open(infile, 'r') as f:
    lines = f.read().strip().splitlines() # first reads the entire file; second removes leading/trailing whitespace, including newlines; third splits the string into a list 
x_vals, y_vals = [], []
for line in lines[1:]:
    x, y = line.split(',') # splits each element in the list based on comma seperator
    x_vals.append(float(x.strip())) # It removes extra white space and convert it to float and then append to the empty list x_vals
    y_vals.append(float(y.strip())) # It removes extra white space and convert it to float and then append to the empty list y_vals
plt.plot(x_vals, y_vals) # plots the line graph
plt.savefig(outfile) # saves in the outfile

#plt.show() and plt.close() # This is not required since it is a .py file but you can close the plot after showing it 