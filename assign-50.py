#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt

def main():
    # check arguments
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} inputfile outputfile")
        sys.exit(1)

    infile = sys.argv[1]
    outfile = sys.argv[2]

    # read input
    with open(infile, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    title = lines[0]  # first line is the title
    data = [line.split(",") for line in lines[1:]]
    x = [float(d[0]) for d in data]
    y = [float(d[1]) for d in data]

    # plot
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel("X")
    plt.ylabel("Y")

    # save figure
    plt.savefig(outfile)

if __name__ == "__main__":
    main()
