import unittest
from unittest.mock import Mock, patch

import nmans
from nmans.config import defaults
from nmans.models import SpectralClass


@patch('nmans._nmans.config.read_config', lambda: defaults.default_config)
class TestSpectralTraits(unittest.TestCase):

    def test_one_trait_returns_one_affices(self):
        class_ = SpectralClass('f9p')
        result = nmans.get_trait_affices(class_)
        self.assertEqual(1, len(result))

    def test_two_traits_returns_two_affices(self):
        class_ = SpectralClass('f9pq')
        result = nmans.get_trait_affices(class_)
        self.assertEqual(2, len(result))

    @patch('nmans._nmans.config.read_config')
    def test_zero_traits_returns_zero_affices(self, mock_config: Mock):
        class_ = SpectralClass('f9')
        result = nmans.get_trait_affices(class_)
        self.assertEqual(0, len(result))
        mock_config.assert_not_called()
