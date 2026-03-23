#!/usr/bin/env python3
import sys
import matplotlib
matplotlib.use("Agg")  
#Uses the Agg backend so you can save figures without opening a GUI window
import matplotlib.pyplot as plt

if len(sys.argv) != 3:
    sys.exit(1)
infile = sys.argv[1]
outfile = sys.argv[2]
with open(infile, 'r') as f:
    lines = f.read().strip().splitlines()
x_vals, y_vals = [], []
for line in lines[1:]:
    x, y = line.split(',')
    x_vals.append(float(x.strip()))
    y_vals.append(float(y.strip()))
    
plt.plot(x_vals, y_vals, label= "No drug") # label is added 
plt.xlabel("Time (min)") # x axis label
plt.ylabel("Cell count") # y axis label
plt.legend(loc="best") # Legend is placed such a way it does not / minimise overlap with the data.
plt.savefig(outfile)
