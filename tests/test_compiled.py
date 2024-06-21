from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

import findmfpy._core as m


def test_pick_peaks():
    mz_arr, int_arr = np.load(Path(__file__).parent / "data" / "sample.npy")
    mz_peak, int_peak = m.pick_peaks(mz_arr, int_arr)

    plt.plot(mz_arr, int_arr)
    plt.scatter(mz_peak, int_peak, color="red", marker="x")
    plt.xlim(1000, 1100)
    plt.savefig("test_pick_peaks.pdf")

    assert len(mz_peak) == len(mz_arr)
