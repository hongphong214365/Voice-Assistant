import unittest

import numpy as np

from audio_processor import calculate_rms


class CalculateRmsTests(unittest.TestCase):
    def test_silence_has_zero_rms(self):
        self.assertEqual(calculate_rms(np.zeros(8, dtype=np.int16)), 0.0)

    def test_constant_signal_has_its_absolute_amplitude(self):
        self.assertEqual(calculate_rms(np.full(8, 120, dtype=np.int16)), 120.0)

    def test_sign_does_not_change_rms(self):
        self.assertAlmostEqual(calculate_rms(np.array([-3, 3], dtype=np.int16)), 3.0)

    def test_int16_extremes_do_not_overflow(self):
        self.assertAlmostEqual(
            calculate_rms(np.array([-32768, 32767], dtype=np.int16)),
            32767.5,
            places=1,
        )

    def test_empty_audio_raises_value_error(self):
        with self.assertRaises(ValueError):
            calculate_rms(np.array([], dtype=np.int16))


if __name__ == "__main__":
    unittest.main()
