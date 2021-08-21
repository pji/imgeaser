"""
test_imgeaser
~~~~~~~~~~~~~
"""
import numpy as np

from imgeaser import imgeaser as ie
from tests.common import ArrayTestCase, A


# Basic test case.
class EaseTestCase(ArrayTestCase):
    def run_test(self, exp, ease, a=None, *args, **kwargs):
        """Run a basic unit test on an easing function."""
        # Test data and state.
        if not a:
            a = A.copy()

        # Run test.
        act = ease(a, *args, **kwargs)

        # Determine test result.
        self.assertArrayEqual(exp, act, round_=True)
        self.assertEqual(exp.dtype, act.dtype)


# Test case.
class EaseInOutSinTestCase(EaseTestCase):
    def test_ease(self):
        """Given an array of image data, run the 'in sine' easing
        function on the data and return the result.
        """
        ease = ie.ease_in_out_sin
        exp = np.array([
            [
                [0.0000, 0.1464, 0.5000, 0.8536, 1.0000],
                [0.1464, 0.5000, 0.8536, 1.0000, 0.8536],
                [0.5000, 0.8536, 1.0000, 0.8536, 0.5000],
                [0.8536, 1.0000, 0.8536, 0.5000, 0.1464],
                [1.0000, 0.8536, 0.5000, 0.1464, 0.0000],
            ],
        ], dtype=np.float32)
        self.run_test(exp, ease)


class EaseInSinTestCase(EaseTestCase):
    def test_ease(self):
        """Given an array of image data, run the 'in sine' easing
        function on the data and return the result.
        """
        ease = ie.ease_in_sin
        exp = np.array([
            [
                [0.0000, 0.0761, 0.2929, 0.6173, 1.0000],
                [0.0761, 0.2929, 0.6173, 1.0000, 0.6173],
                [0.2929, 0.6173, 1.0000, 0.6173, 0.2929],
                [0.6173, 1.0000, 0.6173, 0.2929, 0.0761],
                [1.0000, 0.6173, 0.2929, 0.0761, 0.0000],
            ],
        ], dtype=np.float32)
        self.run_test(exp, ease)


class EaseOutSinTestCase(EaseTestCase):
    def test_ease(self):
        """Given an array of image data, run the 'in sine' easing
        function on the data and return the result.
        """
        ease = ie.ease_out_sin
        exp = np.array([
            [
                [0.0000, 0.3827, 0.7071, 0.9239, 1.0000],
                [0.3827, 0.7071, 0.9239, 1.0000, 0.9239],
                [0.7071, 0.9239, 1.0000, 0.9239, 0.7071],
                [0.9239, 1.0000, 0.9239, 0.7071, 0.3827],
                [1.0000, 0.9239, 0.7071, 0.3827, 0.0000],
            ],
        ], dtype=np.float32)
        self.run_test(exp, ease)
