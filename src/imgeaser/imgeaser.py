"""
imgeaser
~~~~~~~~

Easing functions for image data. Well, they'll work on any numeric data,
but they are written for image data.


Ease In
=======
These functions start slow or extend the darkness in an image:

.. autofunction:: imgeaser.ease_in_back
.. autofunction:: imgeaser.ease_in_circ
.. autofunction:: imgeaser.ease_in_cubic
.. autofunction:: imgeaser.ease_in_elastic
.. autofunction:: imgeaser.ease_in_quad
.. autofunction:: imgeaser.ease_in_quint
.. autofunction:: imgeaser.ease_in_sin


Ease Out
========
These functions start fast or extend the lightness in an image:

.. autofunction:: imgeaser.ease_out_bounce
.. autofunction:: imgeaser.ease_out_circ
.. autofunction:: imgeaser.ease_out_cubic
.. autofunction:: imgeaser.ease_out_elastic
.. autofunction:: imgeaser.ease_out_quad
.. autofunction:: imgeaser.ease_out_quint
.. autofunction:: imgeaser.ease_out_sin


Ease In Out
===========
These functions go fast in the middle or compress the midtones of the image.

.. autofunction:: imgeaser.ease_in_out_back
.. autofunction:: imgeaser.ease_in_out_circ
.. autofunction:: imgeaser.ease_in_out_cos
.. autofunction:: imgeaser.ease_in_out_cubic
.. autofunction:: imgeaser.ease_in_out_elastic
.. autofunction:: imgeaser.ease_in_out_quad
.. autofunction:: imgeaser.ease_in_out_quint
.. autofunction:: imgeaser.ease_in_out_sin


Ease Mid
========
These functions change the values in the data, making the midtones dark
and the edges light.

.. autofunction:: imgeaser.ease_mid_bump_linear
.. autofunction:: imgeaser.ease_mid_bump_sin


Types
=====
The following types are available for creating type hints.

*   :class:`Ease`: A function that follows the "ease function" protocol.
*   :class:`ImgAry`: An :class:`numpy.ndarray` of numeric data to be eased.

"""
from typing import Callable

import numpy as np
from numpy.typing import NDArray

from imgeaser.utility import will_scale


# Types.
ImgAry = NDArray[np.float_]
Ease = Callable[[ImgAry], ImgAry]


# Ease in functions.
@will_scale
def ease_in_back(a: ImgAry) -> ImgAry:
    """An easing function that backs up a little before starting.
    
    .. figure:: images/plot_ease_in_back.png
       :alt: A chart showing the action of the easing function.
       
       The action of :func:`ease_in_back`.
       
    With image data, it extends the darker areas and compresses the
    lighter ones. The dip into negative values can be a little
    awkward. It's left to the calling application to decide how to
    handle it. In the following example, values are just truncated at
    zero.
    
    .. figure:: images/ex_ease_in_back.png
       :alt: An example of the easing function affecting a gradient.
       
       An example of how :func:`ease_in_back` affects a simple gradient. 
    
    :param a: An array of image data.
    :return: The eased data as a :class:`numpy.ndarray`.
    :rtype: numpy.ndarray
    """
    c1 = 1.70158
    c3 = c1 + 1
    return c3 * a ** 3 - c1 * a ** 2


@will_scale
def ease_in_circ(a: ImgAry) -> ImgAry:
    """An easing function that has a circular curve.
    
    .. figure:: images/plot_ease_in_circ.png
       :alt: A chart showing the action of the easing function.
       
       The action of :func:`ease_in_circ`.
       
    With image data, it is a moderate extension of the darker areas
    and compression of the lighter ones. This should not generate
    values outside of the original range.
    
    .. figure:: images/ex_ease_in_circ.png
       :alt: An example of the easing function affecting a gradient.
       
       An example of how :func:`ease_in_circ` affects a simple gradient. 
    
    :param a: An array of image data.
    :return: The eased data as a :class:`numpy.ndarray`.
    :rtype: numpy.ndarray
    """
    return 1 - np.sqrt(1 - a ** 2)


@will_scale
def ease_in_cubic(a: ImgAry) -> ImgAry:
    """An easing function that has a cubic curve.
    
    .. figure:: images/plot_ease_in_cubic.png
       :alt: A chart showing the action of the easing function.
       
       The action of :func:`ease_in_cubic`.
       
    With image data, it is a moderate extension of the darker areas
    and compression of the lighter ones. This should not generate
    values outside of the original range.
    
    .. figure:: images/ex_ease_in_cubic.png
       :alt: An example of the easing function affecting a gradient.
       
       An example of how :func:`ease_in_cubic` affects a simple gradient. 
    
    :param a: An array of image data.
    :return: The eased data as a :class:`numpy.ndarray`.
    :rtype: numpy.ndarray
    """
    return a ** 3


@will_scale
def ease_in_elastic(a: ImgAry) -> ImgAry:
    """An easing function that bounces.
    
    .. figure:: images/plot_ease_in_elastic.png
       :alt: A chart showing the action of the easing function.
       
       The action of :func:`ease_in_elastic`.
       
    With image data, it extends the darker areas and compresses the
    lighter ones. The dip into negative values can be a little
    awkward. It's left to the calling application to decide how to
    handle it. In the following example, values are just truncated at
    zero.
    
    .. figure:: images/ex_ease_in_elastic.png
       :alt: An example of the easing function affecting a gradient.
       
       An example of how :func:`ease_in_elastic` affects a simple gradient. 
    
    :param a: An array of image data.
    :return: The eased data as a :class:`numpy.ndarray`.
    :rtype: numpy.ndarray
    """
    c4 = (2 * np.pi) / 3
    m = np.zeros(a.shape, bool)
    m[a == 0] = True
    m[a == 1] = True
    a[~m] = -(2 ** (10 * a[~m] - 10)) * np.sin((a[~m] * 10 - 10.75) * c4)
    return a


@will_scale
def ease_in_quad(a: ImgAry) -> ImgAry:
    """An easing function that has a quadratic curve.
    
    .. figure:: images/plot_ease_in_quad.png
       :alt: A chart showing the action of the easing function.
       
       The action of :func:`ease_in_quad`.
       
    With image data, it is a moderate extension of the darker areas
    and compression of the lighter ones. This should not generate
    values outside of the original range.
    
    .. figure:: images/ex_ease_in_quad.png
       :alt: An example of the easing function affecting a gradient.
       
       An example of how :func:`ease_in_quad` affects a simple gradient. 
    
    :param a: An array of image data.
    :return: The eased data as a :class:`numpy.ndarray`.
    :rtype: numpy.ndarray
    """
    return a ** 2


@will_scale
def ease_in_quint(a: ImgAry) -> ImgAry:
    """An easing function that has a quintic curve.
    
    .. figure:: images/plot_ease_in_quint.png
       :alt: A chart showing the action of the easing function.
       
       The action of :func:`ease_in_quint`.
       
    With image data, it is a large extension of the darker areas
    and compression of the lighter ones. This should not generate
    values outside of the original range.
    
    .. figure:: images/ex_ease_in_quint.png
       :alt: An example of the easing function affecting a gradient.
       
       An example of how :func:`ease_in_quint` affects a simple gradient. 
    
    :param a: An array of image data.
    :return: The eased data as a :class:`numpy.ndarray`.
    :rtype: numpy.ndarray
    """
    return a ** 5


@will_scale
def ease_in_sin(a: ImgAry) -> ImgAry:
    """An easing function that has a sine curve.
    
    .. figure:: images/plot_ease_in_sin.png
       :alt: A chart showing the action of the easing function.
       
       The action of :func:`ease_in_sin`.
       
    With image data, it is a small extension of the darker areas
    and compression of the lighter ones. This should not generate
    values outside of the original range.
    
    .. figure:: images/ex_ease_in_sin.png
       :alt: An example of the easing function affecting a gradient.
       
       An example of how :func:`ease_in_sin` affects a simple gradient. 
    
    :param a: An array of image data.
    :return: The eased data as a :class:`numpy.ndarray`.
    :rtype: numpy.ndarray
    """
    return 1 - np.cos(a * np.pi / 2)


# Ease out functions.
@will_scale
def ease_out_bounce(a: ImgAry) -> ImgAry:
    """An easing function that has a bounce.
    
    .. figure:: images/plot_ease_out_bounce.png
       :alt: A chart showing the action of the easing function.
       
       The action of :func:`ease_out_bounce`.
       
    With image data, it is a large extension of the lighter areas
    with multiple peaks and compression of the darker ones.
    
    .. figure:: images/ex_ease_out_bounce.png
       :alt: An example of the easing function affecting a gradient.
       
       An example of how :func:`ease_out_bounce` affects a simple gradient. 
    
    :param a: An array of image data.
    :return: The eased data as a :class:`numpy.ndarray`.
    :rtype: numpy.ndarray
    """
    n1 = 7.5625
    d1 = 2.75
    
    b = np.zeros(a.shape, dtype=a.dtype)

    b[a >= 2.5 / d1] = n1 * (a[a >= 2.5 / d1] - 2.625 / d1) ** 2 + .984375
    b[a < 2.5 / d1] = n1 * (a[a < 2.5 / d1] - 2.25 / d1) ** 2 + .9375
    b[a < 2 / d1] = n1 * (a[a < 2 / d1] - 1.5 / d1) ** 2 + .75
    b[a < 1 / d1] = n1 * a[a < 1 / d1] ** 2

    return b


@will_scale
def ease_out_circ(a: ImgAry) -> ImgAry:
    """An easing function that has a circular curve.
    
    .. figure:: images/plot_ease_out_circ.png
       :alt: A chart showing the action of the easing function.
       
       The action of :func:`ease_out_circ`.
       
    With image data, it is a moderate extension of the lighter areas
    and compression of the darker ones.
    
    .. figure:: images/ex_ease_out_circ.png
       :alt: An example of the easing function affecting a gradient.
       
       An example of how :func:`ease_out_circ` affects a simple gradient. 
    
    :param a: An array of image data.
    :return: The eased data as a :class:`numpy.ndarray`.
    :rtype: numpy.ndarray
    """
    return np.sqrt(1 - (a - 1) ** 2)


@will_scale
def ease_out_cubic(a: ImgAry) -> ImgAry:
    """An easing function that has a cubic curve.
    
    .. figure:: images/plot_ease_out_cubic.png
       :alt: A chart showing the action of the easing function.
       
       The action of :func:`ease_out_cubic`.
       
    With image data, it is a moderate extension of the lighter areas
    and compression of the darker ones.
    
    .. figure:: images/ex_ease_out_cubic.png
       :alt: An example of the easing function affecting a gradient.
       
       An example of how :func:`ease_out_cubic` affects a simple gradient. 
    
    :param a: An array of image data.
    :return: The eased data as a :class:`numpy.ndarray`.
    :rtype: numpy.ndarray
    """
    return 1 - (1 - a) ** 3


@will_scale
def ease_out_elastic(a: ImgAry) -> ImgAry:
    """An easing function that bounces.
    
    .. figure:: images/plot_ease_out_elastic.png
       :alt: A chart showing the action of the easing function.
       
       The action of :func:`ease_out_elastic`.
       
    With image data, it extends the lighter areas and compresses the
    darker ones. The bounce into values over one can be a little
    awkward. It's left to the calling application to decide how to
    handle it. In the following example, values are just truncated at
    one.
    
    .. figure:: images/ex_ease_out_elastic.png
       :alt: An example of the easing function affecting a gradient.
       
       An example of how :func:`ease_out_elastic` affects a simple gradient. 
    
    :param a: An array of image data.
    :return: The eased data as a :class:`numpy.ndarray`.
    :rtype: numpy.ndarray
    """
    c4 = (2 * np.pi) / 3
    m = np.zeros(a.shape, bool)
    m[a == 0] = True
    m[a == 1] = True
    a[~m] = 2 ** (-10 * a[~m]) * np.sin((a[~m] * 10 - .75) * c4) + 1
    return a


@will_scale
def ease_out_quad(a: ImgAry) -> ImgAry:
    """An easing function that has a quadratic curve.
    
    .. figure:: images/plot_ease_out_quad.png
       :alt: A chart showing the action of the easing function.
       
       The action of :func:`ease_out_quad`.
       
    With image data, it is a moderate extension of the lighter areas
    and compression of the darker ones.
    
    .. figure:: images/ex_ease_out_quad.png
       :alt: An example of the easing function affecting a gradient.
       
       An example of how :func:`ease_out_quad` affects a simple gradient. 
    
    :param a: An array of image data.
    :return: The eased data as a :class:`numpy.ndarray`.
    :rtype: numpy.ndarray
    """
    return 1 - (1 - a) ** 2


@will_scale
def ease_out_quint(a: ImgAry) -> ImgAry:
    """An easing function that has a quintic curve.
    
    .. figure:: images/plot_ease_out_quint.png
       :alt: A chart showing the action of the easing function.
       
       The action of :func:`ease_out_quint`.
       
    With image data, it is a large extension of the lighter areas
    and compression of the darker ones.
    
    .. figure:: images/ex_ease_out_quint.png
       :alt: An example of the easing function affecting a gradient.
       
       An example of how :func:`ease_out_quint` affects a simple gradient. 
    
    :param a: An array of image data.
    :return: The eased data as a :class:`numpy.ndarray`.
    :rtype: numpy.ndarray
    """
    return 1 - (1 - a) ** 5


@will_scale
def ease_out_sin(a: ImgAry) -> ImgAry:
    """An easing function that has a sine curve.
    
    .. figure:: images/plot_ease_out_sin.png
       :alt: A chart showing the action of the easing function.
       
       The action of :func:`ease_out_sin`.
       
    With image data, it is a small extension of the lighter areas
    and compression of the darker ones.
    
    .. figure:: images/ex_ease_out_sin.png
       :alt: An example of the easing function affecting a gradient.
       
       An example of how :func:`ease_out_sin` affects a simple gradient. 
    
    :param a: An array of image data.
    :return: The eased data as a :class:`numpy.ndarray`.
    :rtype: numpy.ndarray
    """
    return np.sin(a * np.pi / 2)


# Ease in and out functions.
@will_scale
def ease_in_out_back(a: ImgAry) -> ImgAry:
    """An easing function that backs up then overshoots.
    
    .. figure:: images/plot_ease_in_out_back.png
       :alt: A chart showing the action of the easing function.
       
       The action of :func:`ease_in_out_back`.
       
    With image data, it extends the darker and lighter areas. The dip
    into negative values and bounce over one can be a little awkward.
    It's left to the calling application to decide how to handle it. In
    the following example, values are just truncated at zero and one.
    
    .. figure:: images/ex_ease_in_out_back.png
       :alt: An example of the easing function affecting a gradient.
       
       An example of how :func:`ease_in_out_back` affects a simple gradient. 
    
    :param a: An array of image data.
    :return: The eased data as a :class:`numpy.ndarray`.
    :rtype: numpy.ndarray
    """
    c1 = 1.70158
    c2 = c1 * 1.525
    m = np.zeros(a.shape, bool)
    m[a < .5] = True
    a[m] = (2 * a[m]) ** 2 * ((c2 + 1) * 2 * a[m] - c2) / 2
    a[~m] = ((2 * a[~m] - 2) ** 2 * ((c2 + 1) * (a[~m] * 2 - 2) + c2) + 2) / 2
    return a


@will_scale
def ease_in_out_circ(a: ImgAry) -> ImgAry:
    """An easing function that uses a circular curve to compress the
    middle.
    
    .. figure:: images/plot_ease_in_out_circ.png
       :alt: A chart showing the action of the easing function.
       
       The action of :func:`ease_in_out_circ`.
       
    With image data, it extends the darker and lighter areas. This
    should not generate values outside of the original range.
    
    .. figure:: images/ex_ease_in_out_circ.png
       :alt: An example of the easing function affecting a gradient.
       
       An example of how :func:`ease_in_out_circ` affects a simple gradient. 
    
    :param a: An array of image data.
    :return: The eased data as a :class:`numpy.ndarray`.
    :rtype: numpy.ndarray
    """
    m = np.zeros(a.shape, bool)
    m[a < .5] = True
    a[m] = (1 - np.sqrt(1 - (2 * a[m]) ** 2)) / 2
    a[~m] = (np.sqrt(1 - (-2 * a[~m] + 2) ** 2) + 1) / 2
    return a


@will_scale
def ease_in_out_cos(a: ImgAry) -> ImgAry:
    """An easing function that uses a cosine curve to turn the make the
    middle low and the edges high.
    
    .. figure:: images/plot_ease_in_out_cos.png
       :alt: A chart showing the action of the easing function.
       
       The action of :func:`ease_in_out_cos`.
       
    With image data, it turns the midtones dark and the dark and light
    become midtones. This should not generate values outside of the
    original range.
    
    .. figure:: images/ex_ease_in_out_cos.png
       :alt: An example of the easing function affecting a gradient.
       
       An example of how :func:`ease_in_out_cos` affects a simple gradient. 
    
    :param a: An array of image data.
    :return: The eased data as a :class:`numpy.ndarray`.
    :rtype: numpy.ndarray
    """
    return -1 * (np.sin(np.pi * a) - 1) / 2


@will_scale
def ease_in_out_cubic(a: ImgAry) -> ImgAry:
    """An easing function that uses a cubic curve to compress the
    middle.
    
    .. figure:: images/plot_ease_in_out_cubic.png
       :alt: A chart showing the action of the easing function.
       
       The action of :func:`ease_in_out_cubic`.
       
    With image data, it extends the darker and lighter areas. This
    should not generate values outside of the original range.
    
    .. figure:: images/ex_ease_in_out_cubic.png
       :alt: An example of the easing function affecting a gradient.
       
       An example of how :func:`ease_in_out_cubic` affects a simple gradient. 
    
    :param a: An array of image data.
    :return: The eased data as a :class:`numpy.ndarray`.
    :rtype: numpy.ndarray
    """
    a[a < .5] = 4 * a[a < .5] ** 3
    a[a >= .5] = 1 - (-2 * a[a >= .5] + 2) ** 3 / 2
    return a


@will_scale
def ease_in_out_elastic(a: ImgAry) -> ImgAry:
    """An easing function that uses a bouncy curve to compress the
    middle.
    
    .. figure:: images/plot_ease_in_out_elastic.png
       :alt: A chart showing the action of the easing function.
       
       The action of :func:`ease_in_out_elastic`.
       
    With image data, it extends the darker and lighter areas. The 
    dip into values below zero or bounce into values over one can
    be a little awkward. It's left to the calling application to
    decide how to handle it. In the following example, values are
    just truncated at one.
    
    .. figure:: images/ex_ease_in_out_elastic.png
       :alt: An example of the easing function affecting a gradient.
       
       An example of how :func:`ease_in_out_elastic` affects a simple
       gradient. 
    
    :param a: An array of image data.
    :return: The eased data as a :class:`numpy.ndarray`.
    :rtype: numpy.ndarray
    """
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
def ease_in_out_quad(a: ImgAry) -> ImgAry:
    """An easing function that uses a quadratic curve to compress the
    middle.
    
    .. figure:: images/plot_ease_in_out_quad.png
       :alt: A chart showing the action of the easing function.
       
       The action of :func:`ease_in_out_quad`.
       
    With image data, it extends the darker and lighter areas. This
    should not generate values outside of the original range.
    
    .. figure:: images/ex_ease_in_out_quad.png
       :alt: An example of the easing function affecting a gradient.
       
       An example of how :func:`ease_in_out_quad` affects a simple
       gradient. 
    
    :param a: An array of image data.
    :return: The eased data as a :class:`numpy.ndarray`.
    :rtype: numpy.ndarray
    """
    m = np.zeros(a.shape, bool)
    m[a < .5] = True
    a[m] = 2 * a[m] ** 2
    a[~m] = 1 - (-2 * a[~m] + 2) ** 2 / 2
    return a


@will_scale
def ease_in_out_quint(a: ImgAry) -> ImgAry:
    """An easing function that uses a quintic curve to compress the
    middle.
    
    .. figure:: images/plot_ease_in_out_quint.png
       :alt: A chart showing the action of the easing function.
       
       The action of :func:`ease_in_out_quint`.
       
    With image data, it greatly extends the darker and lighter areas.
    This should not generate values outside of the original range.
    
    .. figure:: images/ex_ease_in_out_quint.png
       :alt: An example of the easing function affecting a gradient.
       
       An example of how :func:`ease_in_out_quint` affects a simple
       gradient. 
    
    :param a: An array of image data.
    :return: The eased data as a :class:`numpy.ndarray`.
    :rtype: numpy.ndarray
    """
    a[a < .5] = 16 * a[a < .5] ** 5
    a[a >= .5] = 1 - (-2 * a[a >= .5] + 2) ** 5 / 2
    return a


@will_scale
def ease_in_out_sin(a: ImgAry) -> ImgAry:
    """An easing function that uses a sine curve to compress the
    middle.
    
    .. figure:: images/plot_ease_in_out_sin.png
       :alt: A chart showing the action of the easing function.
       
       The action of :func:`ease_in_out_sin`.
       
    With image data, it slightly extends the darker and lighter areas.
    This should not generate values outside of the original range.
    
    .. figure:: images/ex_ease_in_out_sin.png
       :alt: An example of the easing function affecting a gradient.
       
       An example of how :func:`ease_in_out_sin` affects a simple gradient. 
    
    :param a: An array of image data.
    :return: The eased data as a :class:`numpy.ndarray`.
    :rtype: numpy.ndarray
    """
    return -1 * (np.cos(np.pi * a) - 1) / 2


# Ease mid functions.
@will_scale
def ease_mid_bump_linear(a: ImgAry) -> ImgAry:
    """An easing function that makes the middle of the range the peak
    of the values.
    
    .. figure:: images/plot_ease_mid_bump_linear.png
       :alt: A chart showing the action of the easing function.
       
       The action of :func:`ease_mid_bump_linear`.
       
    With image data, it makes the midtones light and the edges dark.
    
    .. figure:: images/ex_ease_mid_bump_linear.png
       :alt: An example of the easing function affecting a gradient.
       
       An example of how :func:`ease_mid_bump_linear` affects a simple
       gradient. 
    
    :param a: An array of image data.
    :return: The eased data as a :class:`numpy.ndarray`.
    :rtype: numpy.ndarray
    """
    a = np.abs(a - .5)
    m = np.zeros(a.shape, bool)
    m[a < .25] = True
    a[m] = (.25 - a[m]) * 4
    a[~m] = 0
    return a


@will_scale
def ease_mid_bump_sin(a: ImgAry) -> ImgAry:
    """An easing function that makes the middle of the range the peak
    of the values.
    
    .. figure:: images/plot_ease_mid_bump_sin.png
       :alt: A chart showing the action of the easing function.
       
       The action of :func:`ease_mid_bump_sin`.
       
    With image data, it makes the midtones light and the edges dark.
    
    .. figure:: images/ex_ease_mid_bump_sin.png
       :alt: An example of the easing function affecting a gradient.
       
       An example of how :func:`ease_mid_bump_sin` affects a simple
       gradient. 
    
    :param a: An array of image data.
    :return: The eased data as a :class:`numpy.ndarray`.
    :rtype: numpy.ndarray
    """
    a = np.abs(a - .5)
    m = np.zeros(a.shape, bool)
    m[a < .25] = True
    a[m] = (.25 - a[m]) * 4
    a[~m] = 0
    return ease_in_out_sin(a)
