"""
utility
~~~~~~~

Utility functions for the imgeaser module.
"""
from functools import wraps
from typing import Callable

import numpy as np


# Decorators.
def will_scale(fn: Callable) -> Callable:
    @wraps(fn)
    def wrapper(a: np.ndarray, *args, **kwargs) -> np.ndarray:
        # Only scale data that isn't within zero to one.
        scale = None
        scale_offset = None
        if np.min(a) < 0.0 or np.max(a) > 1.0:
            scale_offset = np.min(a)
            a -= scale_offset
            scale = np.max(a)
            a /= scale
        
        # Perform the ease.
        a = fn(a)
        
        # If the data was scaled, undo the scaling.
        if scale or scale_offset:
            a *= scale
            a += scale_offset
        
        return a
    return wrapper


# Debugging utilities.
def print_array(a: np.ndarray, depth: int = 0, color: bool = True) -> None:
    """Write the values of the given array to stdout."""
    if len(a.shape) > 1:
        print(' ' * (4 * depth) + '[')
        for i in range(a.shape[0]):
            print_array(a[i], depth + 1, color)
        print(' ' * (4 * depth) + '],')

    else:
        if a.dtype == np.float32 or a.dtype == np.float64:
            tmp = '{:>1.4f}'
        else:
            tmp = '{}'
        nums = [tmp.format(n) for n in a]
        print(' ' * (4 * depth) + '[' + ', '.join(nums) + '],')


# Sample data.
A = np.array([
    [
        [0.00, 0.25, 0.50, 0.75, 1.00, ],
        [0.25, 0.50, 0.75, 1.00, 0.75, ],
        [0.50, 0.75, 1.00, 0.75, 0.50, ],
        [0.75, 1.00, 0.75, 0.50, 0.25, ],
        [1.00, 0.75, 0.50, 0.25, 0.00, ],
    ],
], dtype=np.float32)
B = np.array([
    [
        [1.00, 0.75, 0.50, 0.25, 0.00, ],
        [0.75, 1.00, 0.75, 0.50, 0.25, ],
        [0.50, 0.75, 1.00, 0.75, 0.50, ],
        [0.25, 0.50, 0.75, 1.00, 0.75, ],
        [0.00, 0.25, 0.50, 0.75, 1.00, ],
    ],
], dtype=np.float32)
C = np.array([
    [
        [0.5000, 0.3750, 0.2500, 0.1250, 0.0000, ],
        [0.3750, 0.2500, 0.1250, 0.0000, 0.1250, ],
        [0.2500, 0.1250, 0.0000, 0.1250, 0.2500, ],
        [0.1250, 0.0000, 0.1250, 0.2500, 0.3750, ],
        [0.0000, 0.1250, 0.2500, 0.3750, 0.5000, ],
    ],
], dtype=np.float32)
D = np.array([
    [
        [0.0000, 0.1250, 0.2500, 0.3750, 0.5000, ],
        [0.1250, 0.0000, 0.1250, 0.2500, 0.3750, ],
        [0.2500, 0.1250, 0.0000, 0.1250, 0.2500, ],
        [0.3750, 0.2500, 0.1250, 0.0000, 0.1250, ],
        [0.5000, 0.3750, 0.2500, 0.1250, 0.0000, ],
    ],
], dtype=np.float32)
E = np.array([
    [
        [0.0, 0.1, 0.2, 0.3, 0.4, ],
        [0.2, 0.3, 0.4, 0.5, 0.6, ],
        [0.4, 0.5, 0.6, 0.7, 0.8, ],
        [0.6, 0.7, 0.8, 0.9, 1.0, ],
        [0.8, 0.9, 1.0, 0.7, 0.8, ],
    ],
], dtype=np.float32)