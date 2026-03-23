#!/usr/bin/env python3
import sys
import matplotlib
matplotlib.use("Agg")   
#Uses the Agg backend so you can save figures without opening a GUI window
import matplotlib.pyplot as plt
# Requires at least 1 input file + 1 output file
if len(sys.argv) < 3:
    sys.exit(1)
    
input_files = sys.argv[1:-1] # Take everything except the last argument as the input file 
output_file = sys.argv[-1]   # The last argument is the name of the output file

for infile in input_files:
    try:
        with open(infile, 'r') as f:
            lines = f.read().strip().splitlines()
        label = lines[0].strip() # First line is used as the legend label
        x_vals, y_vals = [], []
        for line in lines[1:]:
            x, y = line.split(',')
            x_vals.append(float(x.strip()))
            y_vals.append(float(y.strip()))
        plt.plot(x_vals, y_vals, label=label)
    except FileNotFoundError:
        print(f"Error: Input file '{infile}' not found.")
        sys.exit(1)

plt.xlabel("Time (min)")
plt.ylabel("Cell count")
plt.legend(loc="best")
plt.savefig(output_file)