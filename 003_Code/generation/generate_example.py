"""Example generation script: writes data/example.csv."""
from pathlib import Path

import numpy as np

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def main():
    DATA_DIR.mkdir(exist_ok=True)
    x = np.linspace(0, 2 * np.pi, 200)
    np.savetxt(DATA_DIR / "example.csv", np.column_stack([x, np.sin(x)]),
               delimiter=",", header="x,y", comments="")


if __name__ == "__main__":
    main()
