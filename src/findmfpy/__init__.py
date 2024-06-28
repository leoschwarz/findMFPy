"""
Copyright (c) 2024 Leonardo Schwarz. All rights reserved.

findMFPy: Python bindings to findMF
"""

from __future__ import annotations

from .api import pick_peaks, pick_peaks_diagnostic

__version__ = "0.1.0"

__all__ = ["__version__", "pick_peaks", "pick_peaks_diagnostic"]
