"""
test_utility
~~~~~~~~~~~~

Unit tests for the imgeaser.utility module.
"""
import numpy as np
import pytest as pt

import imgeaser.utility as u


# Tests for get_prefixed_functions.
def test_get_prefixed_functions():
    """When given a prefix and an object, :func:`get_prefixed_functions`
    should return a :class:`dict` of functions within that object's
    namespace that start with the prefix.
    """
    from tests import spam
    assert u.get_prefixed_functions('spam_', spam) == {
        'eggs': spam.spam_eggs,
        'bacon': spam.spam_bacon,
        'baked_beans': spam.spam_baked_beans,
    }


# fixtures for will_scale.
@pt.fixture
def decorated():
    """A decorated function for testing."""
    @u.will_scale
    def spam(a):
        return a * 0.5

    yield spam


# Tests for will_scale.
def test_will_scale(decorated):
    """When decorating a function, :func:`will_scale` scale the values
    in the array to be within the range of zero to one inclusive.
    """

    a = np.array([
        [
            [2.0, 2.5, 3.0, 3.5, 4.0,],
            [2.0, 2.5, 3.0, 3.5, 4.0,],
            [2.0, 2.5, 3.0, 3.5, 4.0,],
            [2.0, 2.5, 3.0, 3.5, 4.0,],
            [2.0, 2.5, 3.0, 3.5, 4.0,],
        ],
    ], dtype=float)
    assert (decorated(a) == np.array([
        [
            [2.00, 2.25, 2.50, 2.75, 3.00,],
            [2.00, 2.25, 2.50, 2.75, 3.00,],
            [2.00, 2.25, 2.50, 2.75, 3.00,],
            [2.00, 2.25, 2.50, 2.75, 3.00,],
            [2.00, 2.25, 2.50, 2.75, 3.00,],
        ],
    ], dtype=float)).all()


def test_will_scale_no_scale(decorated):
    """When decorating a function, :func:`will_scale` if the values are
    already between zero and one inclusive, don't change the scale.
    """
    a = np.array([
        [
            [0.25, 0.50, 0.75, ],
            [0.25, 0.50, 0.75, ],
            [0.25, 0.50, 0.75, ],
        ],
    ], dtype=float)
    assert (decorated(a) == np.array([
        [
            [0.1250, 0.2500, 0.3750, ],
            [0.1250, 0.2500, 0.3750, ],
            [0.1250, 0.2500, 0.3750, ],
        ],
    ], dtype=float)).all()
