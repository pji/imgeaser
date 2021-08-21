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
