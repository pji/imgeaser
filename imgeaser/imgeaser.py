"""
imgeaser
~~~~~~~~

Easing functions for image data.
"""
import numpy as np

from imgeaser.utility import will_scale


# Ease in functions.
@will_scale
def ease_in_sin(a: np.ndarray) -> np.ndarray:
    return 1 - np.cos(a * np.pi / 2)


# Ease out functions.
@will_scale
def ease_out_sin(a: np.ndarray) -> np.ndarray:
    return np.sin(a * np.pi / 2)


# Ease in and out functions.
def ease_in_out_sin(a: np.ndarray) -> np.ndarray:
    return -1 * (np.cos(np.pi * a) - 1) / 2


if __name__ == '__main__':
    from imgeaser.utility import print_array, A
    
    ease = ease_in_out_sin
    a = A.copy()
    eased = ease(a)
    print_array(eased, depth=2)
    