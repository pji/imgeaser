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
def ease_out_bounce(a: np.ndarray) -> np.ndarray:
    n1 = 7.5625
    d1 = 2.75

    a[a < 1 / d1] = n1 * a[a < 1 / d1] ** 2
    a[a < 2 / d1] = n1 * (a[a < 2 / d1] - 1.5 / d1) ** 2 + .75
    a[a < 2.5 / d1] = n1 * (a[a < 2.5 / d1] - 2.25 / d1) ** 2 + .9375
    a[a >= 2.5 / d1] = n1 * (a[a >= 2.5 / d1] - 2.625 / d1) ** 2 + .984375

    return a


@will_scale
def ease_out_circ(a: np.ndarray) -> np.ndarray:
    return np.sqrt(1 - (a - 1) ** 2)


@will_scale
def ease_out_cubic(a: np.ndarray) -> np.ndarray:
    return 1 - (1 - a) ** 3


@will_scale
def ease_out_elastic(a: np.ndarray) -> np.ndarray:
    c4 = (2 * np.pi) / 3
    m = np.zeros(a.shape, bool)
    m[a == 0] = True
    m[a == 1] = True
    a[~m] = 2 ** (-10 * a[~m]) * np.sin((a[~m] * 10 - .75) * c4) + 1
    return a


@will_scale
def ease_out_quad(a: np.ndarray) -> np.ndarray:
    return 1 - (1 - a) ** 2


@will_scale
def ease_out_quint(a: np.ndarray) -> np.ndarray:
    return 1 - (1 - a) ** 5


@will_scale
def ease_out_sin(a: np.ndarray) -> np.ndarray:
    return np.sin(a * np.pi / 2)


# Ease in and out functions.
@will_scale
def ease_in_out_back(a: np.ndarray) -> np.ndarray:
    c1 = 1.70158
    c2 = c1 * 1.525
    m = np.zeros(a.shape, bool)
    m[a < .5] = True
    a[m] = (2 * a[m]) ** 2 * ((c2 + 1) * 2 * a[m] - c2) / 2
    a[~m] = ((2 * a[~m] - 2) ** 2 * ((c2 + 1) * (a[~m] * 2 - 2) + c2) + 2) / 2
    return a


@will_scale
def ease_in_out_circ(a: np.ndarray) -> np.ndarray:
    m = np.zeros(a.shape, bool)
    m[a < .5] = True
    a[m] = (1 - np.sqrt(1 - (2 * a[m]) ** 2)) / 2
    a[~m] = (np.sqrt(1 - (-2 * a[~m] + 2) ** 2) + 1) / 2
    return a


@will_scale
def ease_in_out_cos(a: np.ndarray) -> np.ndarray:
    return -1 * (np.sin(np.pi * a) - 1) / 2


@will_scale
def ease_in_out_cubic(a: np.ndarray) -> np.ndarray:
    """Perform the in out cubic easing function on the array."""
    a[a < .5] = 4 * a[a < .5] ** 3
    a[a >= .5] = 1 - (-2 * a[a >= .5] + 2) ** 3 / 2
    return a


@will_scale
def ease_in_out_elastic(a: np.ndarray) -> np.ndarray:
    c5 = (2 * np.pi) / 4.5

    # Create masks for the array.
    m1 = np.zeros(a.shape, bool)
    m1[a < .5] = True
    m1[a <= 0] = False
    m2 = np.zeros(a.shape, bool)
    m2[a >= .5] = True
    m2[a >= 1] = False

    # Run the easing function based on the masks.
    a[m1] = -(2 ** (20 * a[m1] - 10) * np.sin((20 * a[m1] - 11.125) * c5))
    a[m1] = a[m1] / 2
    a[m2] = (2 ** (-20 * a[m2] + 10) * np.sin((20 * a[m2] - 11.125) * c5))
    a[m2] = a[m2] / 2 + 1
    return a


@will_scale
def ease_in_out_quad(a: np.ndarray) -> np.ndarray:
    m = np.zeros(a.shape, bool)
    m[a < .5] = True
    a[m] = 2 * a[m] ** 2
    a[~m] = 1 - (-2 * a[~m] + 2) ** 2 / 2
    return a


@will_scale
def ease_in_out_quint(a: np.ndarray) -> np.ndarray:
    """Perform the in out quint function on the array."""
    a[a < .5] = 16 * a[a < .5] ** 5
    a[a >= .5] = 1 - (-2 * a[a >= .5] + 2) ** 5 / 2
    return a


@will_scale
def ease_in_out_sin(a: np.ndarray) -> np.ndarray:
    return -1 * (np.cos(np.pi * a) - 1) / 2


# Ease mid functions.
@will_scale
def ease_mid_bump_linear(a: np.ndarray) -> np.ndarray:
    a = np.abs(a - .5)
    m = np.zeros(a.shape, bool)
    m[a < .25] = True
    a[m] = (.25 - a[m]) * 4
    a[~m] = 0
    return a


@will_scale
def ease_mid_bump_sin(a: np.ndarray) -> np.ndarray:
    a = np.abs(a - .5)
    m = np.zeros(a.shape, bool)
    m[a < .25] = True
    a[m] = (.25 - a[m]) * 4
    a[~m] = 0
    return ease_in_out_sin(a)


if __name__ == '__main__':
    from imgeaser.utility import print_array, A, E

    ease = ease_mid_bump_sin
    a = E.copy()
    eased = ease(a)
    print_array(eased, depth=2)
