"""
imgeaser
~~~~~~~~

Easing functions for image data.
"""
import numpy as np

from imgeaser.utility import will_scale


# Ease in functions.
@will_scale
def ease_in_back(a: np.ndarray) -> np.ndarray:
    c1 = 1.70158
    c3 = c1 + 1
    return c3 * a ** 3 - c1 * a ** 2


@will_scale
def ease_in_circ(a: np.ndarray) -> np.ndarray:
    return 1 - np.sqrt(1 - a ** 2)


@will_scale
def ease_in_cubic(a: np.ndarray) -> np.ndarray:
    return a ** 3


@will_scale
def ease_in_elastic(a: np.ndarray) -> np.ndarray:
    c4 = (2 * np.pi) / 3
    m = np.zeros(a.shape, bool)
    m[a == 0] = True
    m[a == 1] = True
    a[~m] = -(2 ** (10 * a[~m] - 10)) * np.sin((a[~m] * 10 - 10.75) * c4)
    return a


@will_scale
def ease_in_quad(a: np.ndarray) -> np.ndarray:
    return a ** 2


@will_scale
def ease_in_quint(a: np.ndarray) -> np.ndarray:
    return a ** 5


@will_scale
def ease_in_sin(a: np.ndarray) -> np.ndarray:
    return 1 - np.cos(a * np.pi / 2)


# Ease out functions.
@will_scale
def ease_out_sin(a: np.ndarray) -> np.ndarray:
    return np.sin(a * np.pi / 2)


# Ease in and out functions.
@will_scale
def ease_in_out_sin(a: np.ndarray) -> np.ndarray:
    return -1 * (np.cos(np.pi * a) - 1) / 2


if __name__ == '__main__':
    from imgeaser.utility import print_array, A
    
    ease = ease_in_quint
    a = A.copy()
    eased = ease(a)
    print_array(eased, depth=2)
    