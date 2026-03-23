#!/usr/bin/env python3
import sys
import matplotlib
matplotlib.use("Agg")
#Uses the Agg backend so you can save figures without opening a GUI window
import matplotlib.pyplot as plt
import numpy as np

if len(sys.argv) < 3:
    sys.exit(1)

input_files = sys.argv[1:-1]
output_file = sys.argv[-1]

for infile in input_files:
    try:
        with open(infile, 'r') as f:
            lines = f.read().strip().splitlines()
        label = lines[0].strip() 
        x_vals, y_vals_mean, y_vals_std = [], [], []

        for line in lines[1:]:
            parts = [float(x.strip()) for x in line.split(',')]
            x_vals.append(parts[0]) 
            replicates = parts[1:]  
            y_vals_mean.append(np.mean(replicates))
            y_vals_std.append(np.std(replicates))
        plt.errorbar(x_vals, y_vals_mean, yerr=y_vals_std, label=label, capsize=0)

    except FileNotFoundError:
        print(f"Error: Input file '{infile}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error processing file '{infile}': {e}")
        sys.exit(1)

plt.xlabel("Time (min)")
plt.ylabel("Cell count")
plt.legend(loc="best")
plt.savefig(output_file)