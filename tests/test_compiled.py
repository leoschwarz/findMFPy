# from __future__ import annotations
#
# from pathlib import Path
#
# import numpy as np
#
# import findmfpy._core as m
#
#
# def test_pick_peaks():
#    mz_arr, int_arr = np.load(Path(__file__).parent / "data" / "sample.npy")
#    mz_peak, int_peak = m.pick_peaks(mz_arr, int_arr, 10000, 2, 2, 10, True, 0)
#    assert len(mz_peak) == 1392
#    assert len(int_peak) == 1392
#
