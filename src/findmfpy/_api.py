from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

from findmfpy import _core


def _validate_inputs(
    mz_arr: NDArray[np.float64],
    int_arr: NDArray[np.float64],
    resolution: float,
    width: float,
    int_width: float,
    int_threshold: float,
    area: bool,
    max_peaks: int,
) -> tuple[NDArray[np.float64], NDArray[np.float64], float, float, float, float, bool, int]:
    """Validates the inputs to the pick_peaks function."""
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
    return mz_arr, int_arr, resolution, width, int_width, int_threshold, area, max_peaks


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
    """Picks peaks from a mass spectrum.

    Args:
        mz_arr: The m/z array.
        int_arr: The intensity array.
        resolution: The resolution of the instrument.
        width: The width of the peak.
        int_width: The width of the intensity.
        int_threshold: The intensity threshold.
        area: Whether to calculate the area instead of intensity.
        max_peaks: The maximum number of peaks to return.

    Returns:
        0: The m/z array of the peaks.
        1: The intensity array of the peaks.
    """
    mz_arr, int_arr, resolution, width, int_width, int_threshold, area, max_peaks = _validate_inputs(
        mz_arr, int_arr, resolution, width, int_width, int_threshold, area, max_peaks
    )

    # call the c++ function
    mz_arr, int_arr = _core.pick_peaks(mz_arr, int_arr, resolution, width, int_width, int_threshold, area, max_peaks)
    # (making mypy happy)
    return np.asarray(mz_arr), np.asarray(int_arr)


def pick_peaks_diagnostic(
    mz_arr: NDArray[np.float64],
    int_arr: NDArray[np.float64],
    resolution: float = 10000.0,
    width: float = 2.0,
    int_width: float = 2.0,
    int_threshold: float = 10.0,
    area: bool = True,
    max_peaks: int = 0,
) -> tuple[NDArray[np.float64], NDArray[np.float64], dict[str, NDArray[np.float64]]]:
    """Picks peaks from a mass spectrum, and returns some additional diagnostic information of the peak picker.

    Args:
        mz_arr: The m/z array.
        int_arr: The intensity array.
        resolution: The resolution of the instrument.
        width: The width of the peak.
        int_width: The width of the intensity.
        int_threshold: The intensity threshold.
        area: Whether to calculate the area instead of intensity.
        max_peaks: The maximum number of peaks to return.

    Returns:
        0: The m/z array of the peaks.
        1: The intensity array of the peaks.
        2: Diagnostic information from the peak picker internals.
    """
    mz_arr, int_arr, resolution, width, int_width, int_threshold, area, max_peaks = _validate_inputs(
        mz_arr, int_arr, resolution, width, int_width, int_threshold, area, max_peaks
    )

    # call the c++ function
    diagnostics = {}
    (
        mz_arr,
        int_arr,
        diagnostics["resampled_mz_arr"],
        diagnostics["resampled_int_arr"],
        diagnostics["smoothed_int_arr"],
    ) = _core.pick_peaks_diagnostic(mz_arr, int_arr, resolution, width, int_width, int_threshold, area, max_peaks)
    diagnostics = {k: np.asarray(v) for k, v in diagnostics.items()}
    return np.asarray(mz_arr), np.asarray(int_arr), diagnostics
