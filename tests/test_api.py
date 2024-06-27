from __future__ import annotations

from pathlib import Path

import numpy as np

from findmfpy.api import pick_peaks


def test_pick_peaks_when_defaults():
    mz_arr, int_arr = np.load(Path(__file__).parent / "data" / "sample.npy")
    mz_peak, int_peak = pick_peaks(mz_arr, int_arr)
    assert len(mz_peak) == 1392
    assert len(int_peak) == 1392
