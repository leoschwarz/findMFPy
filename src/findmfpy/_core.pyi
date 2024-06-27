from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

def pick_peaks(
    _mz_arr: NDArray[np.float64],
    _int_arr: NDArray[np.float64],
    _resolution: float,
    _width: float,
    _int_width: float,
    _int_threshold: float,
    _area: bool,
    _max_peaks: int,
) -> tuple[NDArray[np.float64], NDArray[np.float64]]: ...
