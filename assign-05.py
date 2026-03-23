#!/usr/bin/env python3

import sys
import numpy as np
import matplotlib.pyplot as plt

def read_data(filename):
    """Read file and return label, x, mean, std (sample std)."""
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    label = lines[0].strip()  # first line = legend
    data = [list(map(float, line.split(","))) for line in lines[1:]]
    data = np.array(data)

    x = data[:, 0]
    y = data[:, 1:]

    means = np.mean(y, axis=1)
    stds = np.std(y, axis=1, ddof=0)

    return label, x, means, stds

def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} infile1 [infile2 ... infileN] outfile")
        sys.exit(1)

    infiles = sys.argv[1:-1]
    outfile = sys.argv[-1]

    for infile in infiles:
        label, x, means, stds = read_data(infile)
        plt.errorbar(x, means, yerr=stds, label=label, capsize=0)

    plt.xlabel("Time (min)")
    plt.ylabel("Cell count")
    plt.legend(loc="best")
    plt.savefig(outfile)

if __name__ == "__main__":
    main()
