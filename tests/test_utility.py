"""
test_utility
~~~~~~~~~~~~

Unit tests for the imgeaser.utility module.
"""
import numpy as np

from common import ArrayTestCase
import imgeaser.utility as u


# Test case.
class WillScaleTestCase(ArrayTestCase):
    def test_scale(self):
        """When decorating a function, scale the values in the array
        to be within the range of zero to one inclusive.
        """
        # Expected value.
        exp = np.array([
            [
                [2.00, 2.25, 2.50, 2.75, 3.00, ],
                [2.00, 2.25, 2.50, 2.75, 3.00, ],
                [2.00, 2.25, 2.50, 2.75, 3.00, ],
                [2.00, 2.25, 2.50, 2.75, 3.00, ],
                [2.00, 2.25, 2.50, 2.75, 3.00, ],
            ],
        ], dtype=np.float32)

        # Test data and state.
        a = np.array([
            [
                [2.0, 2.5, 3.0, 3.5, 4.0, ],
                [2.0, 2.5, 3.0, 3.5, 4.0, ],
                [2.0, 2.5, 3.0, 3.5, 4.0, ],
                [2.0, 2.5, 3.0, 3.5, 4.0, ],
                [2.0, 2.5, 3.0, 3.5, 4.0, ],
            ],
        ], dtype=np.float32)

        @u.will_scale
        def spam(a):
            return a * .5

        # Run test.
        act = spam(a)

        # Determine test result.
        self.assertArrayEqual(exp, act)

    def test_no_scale(self):
        """When decorating a function, if the values are already
        between zero and one inclusive, don't change the scale.
        """
        # Expected value.
        exp = np.array([
            [
                [0.1250, 0.2500, 0.3750, ],
                [0.1250, 0.2500, 0.3750, ],
                [0.1250, 0.2500, 0.3750, ],
            ],
        ], dtype=np.float32)

        # Test data and state.
        a = np.array([
            [
                [0.25, 0.50, 0.75, ],
                [0.25, 0.50, 0.75, ],
                [0.25, 0.50, 0.75, ],
            ],
        ], dtype=np.float32)

        @u.will_scale
        def spam(a):
            return a * .5

        # Run test.
        act = spam(a)

        # Determine test result.
        self.assertArrayEqual(exp, act)
