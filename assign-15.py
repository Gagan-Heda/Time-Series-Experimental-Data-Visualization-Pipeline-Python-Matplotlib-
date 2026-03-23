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
    # check args
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} infile1 [infile2] outfile")
        sys.exit(1)

    infile1 = sys.argv[1]
    outfile = sys.argv[-1]

    # read first dataset
    label1, x1, y1 = read_data(infile1)
    plt.plot(x1, y1, label=label1)

    # optional second dataset
    if len(sys.argv) == 4:
        infile2 = sys.argv[2]
        label2, x2, y2 = read_data(infile2)
        plt.plot(x2, y2, label=label2)

    # labels + legend
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend(loc="best")

    # save
    plt.savefig(outfile)

if __name__ == "__main__":
    main()