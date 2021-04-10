import unittest
from unittest.mock import Mock, patch

import nmans
from nmans.exceptions import NmansException
from nmans.models import SpectralClass


class TestSpectralClassification(unittest.TestCase):

    def test_valid(self):
        result = nmans.is_valid('o0p')
        self.assertTrue(result)

    def test_invalid(self):
        result = nmans.is_valid('!@#$%^&*()`~')
        self.assertFalse(result)

    def test_spectral_name(self):
        class_ = SpectralClass('f9p')
        result = nmans.get_spectral_name(class_)
        self.assertIsNotNone(result)

    def test_spectral_name_invalid(self):
        class_ = SpectralClass('f0')
        class_.spectral_subtype = 10
        self.assertRaises(KeyError, nmans.get_spectral_name, class_)

    def test_trait_affices_none(self):
        class_ = SpectralClass('f9')
        result = nmans.get_trait_affices(class_)
        self.assertTupleEqual((), result)

    def test_trait_affices_one(self):
        class_ = SpectralClass('f9p')
        result = nmans.get_trait_affices(class_)
        self.assertEqual(1, len(result))

    def test_trait_affices_two(self):
        class_ = SpectralClass('f9pw')
        result = nmans.get_trait_affices(class_)
        self.assertEqual(2, len(result))

    @patch('nmans._nmans.portmanteaur')
    def test_system_name(self, mock_portmanteaur: Mock):
        class_ = SpectralClass('o0pw')
        result = nmans.get_system_name('region', class_)
        mock_portmanteaur.get_words.assert_not_called()
        mock_portmanteaur.get_word.assert_called_once()
        self.assertEqual(3, len(result.split('-')))


if __name__ == '__main__':
    unittest.main()
