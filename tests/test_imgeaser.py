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
class EaseInBackTestCase(EaseTestCase):
    def test_ease(self):
        """Given an array of image data, run the 'in back' easing
        function on the data and return the result.
        """
        ease = ie.ease_in_back
        exp = np.array([
            [
                [0.0000, -0.0641, -0.0877, 0.1826, 1.0000],
                [-0.0641, -0.0877, 0.1826, 1.0000, 0.1826],
                [-0.0877, 0.1826, 1.0000, 0.1826, -0.0877],
                [0.1826, 1.0000, 0.1826, -0.0877, -0.0641],
                [1.0000, 0.1826, -0.0877, -0.0641, 0.0000],
            ],
        ], dtype=np.float32)
        self.run_test(exp, ease)


class EaseInCircTestCase(EaseTestCase):
    def test_ease(self):
        """Given an array of image data, run the 'in circ' easing
        function on the data and return the result.
        """
        ease = ie.ease_in_circ
        exp = np.array([
            [
                [0.0000, 0.0318, 0.1340, 0.3386, 1.0000],
                [0.0318, 0.1340, 0.3386, 1.0000, 0.3386],
                [0.1340, 0.3386, 1.0000, 0.3386, 0.1340],
                [0.3386, 1.0000, 0.3386, 0.1340, 0.0318],
                [1.0000, 0.3386, 0.1340, 0.0318, 0.0000],
            ],
        ], dtype=np.float32)
        self.run_test(exp, ease)


class EaseInCubicTestCase(EaseTestCase):
    def test_ease(self):
        """Given an array of image data, run the 'in cubic' easing
        function on the data and return the result.
        """
        ease = ie.ease_in_cubic
        exp = np.array([
            [
                [0.0000, 0.0156, 0.1250, 0.4219, 1.0000],
                [0.0156, 0.1250, 0.4219, 1.0000, 0.4219],
                [0.1250, 0.4219, 1.0000, 0.4219, 0.1250],
                [0.4219, 1.0000, 0.4219, 0.1250, 0.0156],
                [1.0000, 0.4219, 0.1250, 0.0156, 0.0000],
            ],
        ], dtype=np.float32)
        self.run_test(exp, ease)


class EaseInElasticTestCase(EaseTestCase):
    def test_ease(self):
        """Given an array of image data, run the 'in elastic' easing
        function on the data and return the result.
        """
        ease = ie.ease_in_elastic
        exp = np.array([
            [
                [0.0000, -0.0055, -0.0156, 0.0884, 1.0000],
                [-0.0055, -0.0156, 0.0884, 1.0000, 0.0884],
                [-0.0156, 0.0884, 1.0000, 0.0884, -0.0156],
                [0.0884, 1.0000, 0.0884, -0.0156, -0.0055],
                [1.0000, 0.0884, -0.0156, -0.0055, 0.0000],
            ],
        ], dtype=np.float32)
        self.run_test(exp, ease)


class EaseInQuadTestCase(EaseTestCase):
    def test_ease(self):
        """Given an array of image data, run the 'in quad' easing
        function on the data and return the result.
        """
        ease = ie.ease_in_quad
        exp = np.array([
            [
                [0.0000, 0.0625, 0.2500, 0.5625, 1.0000],
                [0.0625, 0.2500, 0.5625, 1.0000, 0.5625],
                [0.2500, 0.5625, 1.0000, 0.5625, 0.2500],
                [0.5625, 1.0000, 0.5625, 0.2500, 0.0625],
                [1.0000, 0.5625, 0.2500, 0.0625, 0.0000],
            ],
        ], dtype=np.float32)
        self.run_test(exp, ease)


class EaseInQuintTestCase(EaseTestCase):
    def test_ease(self):
        """Given an array of image data, run the 'in quint' easing
        function on the data and return the result.
        """
        ease = ie.ease_in_quint
        exp = np.array([
            [
                [0.0000, 0.0010, 0.0312, 0.2373, 1.0000],
                [0.0010, 0.0312, 0.2373, 1.0000, 0.2373],
                [0.0312, 0.2373, 1.0000, 0.2373, 0.0312],
                [0.2373, 1.0000, 0.2373, 0.0312, 0.0010],
                [1.0000, 0.2373, 0.0312, 0.0010, 0.0000],
            ],
        ], dtype=np.float32)
        self.run_test(exp, ease)


class EaseInOutSinTestCase(EaseTestCase):
    def test_ease(self):
        """Given an array of image data, run the 'in out sine' easing
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
        """Given an array of image data, run the 'out sine' easing
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
