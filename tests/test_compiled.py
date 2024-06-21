from __future__ import annotations

from pathlib import Path

import numpy as np

import findmfpy._core as m


def test_add():
    assert m.add(2, 3) == 5


def test_subtract():
    assert m.subtract(7, 5) == 2


def test_pick_peaks():
    mz_arr, int_arr = np.load(Path(__file__).parent / "data" / "sample.npy")
    print(mz_arr)
    print(int_arr)

    mz_peak, int_peak = m.pick_peaks(mz_arr, int_arr)

    print(mz_peak)
    print(int_arr)

    assert len(mz_peak) == len(mz_arr)
