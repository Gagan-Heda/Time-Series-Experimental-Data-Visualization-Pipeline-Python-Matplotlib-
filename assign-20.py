#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt

def main():
    # check args
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} inputfile outputfile")
        sys.exit(1)

    infile = sys.argv[1]
    outfile = sys.argv[2]

    # read file
    with open(infile, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    label = lines[0]   # first line is the label for legend
    data = [line.split(",") for line in lines[1:]]
    x = [float(d[0]) for d in data]
    y = [float(d[1]) for d in data]

    # plot
    plt.plot(x, y, label=label)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend(loc="best")

    # save
    plt.savefig(outfile)

if __name__ == "__main__":
    main()
