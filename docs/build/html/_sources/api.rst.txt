##########
Public API
##########

The following are the classes that make up the public API
of :mod:`imgeaser`.


Easing Functions
================
The following is true of all easing functions:

*   They take a :class:`numpy.ndarray` of numeric data.
*   They return a :class:`numpy.ndarray` of numeric data.
*   If the numeric data is outside of the range of `0 <= x <= 1`, they
    will adjust the data to bring it into that range before performing
    the ease. Then they will return the data to the original range.

All easing functions are registered in the :class:`dict` `imgeaser.eases`
for convenience, but they can also be called directly.


Ease In
-------
These functions start slow or extend the darkness in an image:

.. autofunction:: imgeaser.ease_in_back
.. autofunction:: imgeaser.ease_in_circ
.. autofunction:: imgeaser.ease_in_cubic
.. autofunction:: imgeaser.ease_in_elastic
.. autofunction:: imgeaser.ease_in_quad
.. autofunction:: imgeaser.ease_in_quint
.. autofunction:: imgeaser.ease_in_sin


Ease Out
--------
These functions start fast or extend the lightness in an image:

.. autofunction:: imgeaser.ease_out_bounce
.. autofunction:: imgeaser.ease_out_circ
.. autofunction:: imgeaser.ease_out_cubic
.. autofunction:: imgeaser.ease_out_elastic
.. autofunction:: imgeaser.ease_out_quad
.. autofunction:: imgeaser.ease_out_quint
.. autofunction:: imgeaser.ease_out_sin


Ease In Out
-----------
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
--------
These functions change the values in the data, making the midtones dark
and the edges light.

.. autofunction:: imgeaser.ease_mid_bump_linear
.. autofunction:: imgeaser.ease_mid_bump_sin


Types
=====
The following types are available for creating type hints.

*   :class:`Ease`: A function that follows the "ease function" protocol.
*   :class:`ImgAry`: An :class:`numpy.ndarray` of numeric data to be eased.
