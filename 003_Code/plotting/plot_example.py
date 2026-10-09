"""Example plotting script: reads data/example.csv, writes 002_Figures/example.pdf."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[2]


def main():
    x, y = np.loadtxt(ROOT / "003_Code" / "data" / "example.csv",
                      delimiter=",", skiprows=1, unpack=True)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    fig.savefig(ROOT / "002_Figures" / "example.pdf")


if __name__ == "__main__":
    main()
