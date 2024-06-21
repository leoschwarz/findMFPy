from __future__ import annotations

import importlib.metadata

import findmfpy as m


def test_version():
    assert importlib.metadata.version("findmfpy") == m.__version__
