#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt

def read_data(filename):
    """Read a file and return (label, x, y)."""
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    label = lines[0]
    data = [line.split(",") for line in lines[1:]]
    x = [float(d[0]) for d in data]
    y = [float(d[1]) for d in data]
    return label, x, y

def main():
    # must have at least one input + one output
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} infile1 [infile2 ... infileN] outfile")
        sys.exit(1)

    infiles = sys.argv[1:-1]
    outfile = sys.argv[-1]

    # read & plot each dataset
    for infile in infiles:
        label, x, y = read_data(infile)
        plt.plot(x, y, label=label)

    # labels + legend
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend(loc="best")

    # save
    plt.savefig(outfile)

if __name__ == "__main__":
    main()
