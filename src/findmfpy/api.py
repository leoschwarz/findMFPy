from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

from findmfpy import _core


def pick_peaks(
    mz_arr: NDArray[np.float64],
    int_arr: NDArray[np.float64],
    resolution: float = 10000.0,
    width: float = 2.0,
    int_width: float = 2.0,
    int_threshold: float = 10.0,
    area: bool = True,
    max_peaks: int = 0,
) -> tuple[NDArray[np.float64], NDArray[np.float64]]:
    """
    Pick peaks from a mass spectrum.

    Parameters
    ----------
    mz_arr : numpy.ndarray
        The m/z array.
    int_arr : numpy.ndarray
        The intensity array.
    resolution : float, optional
        The resolution of the instrument, by default 10000.0
    width : float, optional
        The width of the peak, by default 2.0
    int_width : float, optional
        The width of the intensity, by default 2.0
    int_threshold : float, optional
        The intensity threshold, by default 10.0
    area : bool, optional
        Whether to calculate the area instead of intensity, by default True
    max_peaks : int, optional
        The maximum number of peaks to return, by default 0

    Returns
    -------
    tuple[numpy.ndarray, numpy.ndarray]
        The m/z and intensity arrays of the peaks.
    """
    # validate inputs extensively, as passing invalid data to the c++ code can segfault!
    # some of the conversions would be handled automatically by pybind11
    mz_arr = np.ascontiguousarray(np.asarray(mz_arr, dtype=float))
    int_arr = np.ascontiguousarray(np.asarray(int_arr, dtype=float))
    if mz_arr.shape != int_arr.shape:
        msg = f"{mz_arr.shape=} is not equal to {int_arr.shape=}"
        raise ValueError(msg)
    if mz_arr.ndim != 1:
        msg = f"{mz_arr.ndim=} is not 1"
        raise ValueError(msg)
    resolution = float(resolution)
    width = float(width)
    int_width = float(int_width)
    int_threshold = float(int_threshold)
    area = bool(area)
    max_peaks = int(max_peaks)

    # call the c++ function
    mz_arr, int_arr = _core.pick_peaks(mz_arr, int_arr, resolution, width, int_width, int_threshold, area, max_peaks)
    # (making mypy happy)
    return np.asarray(mz_arr), np.asarray(int_arr)
