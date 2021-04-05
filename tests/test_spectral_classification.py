import unittest
from unittest.mock import Mock, patch

import nmans
from nmans.models import SpectralClassification
from nmans.exceptions import NmansException


class TestSpectralClassification(unittest.TestCase):

    def test_valid(self):
        class_ = SpectralClassification('f9p')
        result = nmans.is_valid(class_)
        self.assertTrue(result)

    def test_invalid(self):
        class_ = SpectralClassification('f9z')  # 'z' is not a valid trait.
        result = nmans.is_valid(class_)
        self.assertFalse(result)

    def test_spectral_name(self):
        class_ = SpectralClassification('f9p')
        result = nmans.get_spectral_name(class_)
        self.assertIsNotNone(result)

    def test_spectral_name_invalid(self):
        class_ = SpectralClassification('f0')
        class_.spectral_subtype = 10
        self.assertRaises(KeyError, nmans.get_spectral_name, class_)

    def test_trait_affices_none(self):
        class_ = SpectralClassification('f9')
        result = nmans.get_trait_affices(class_)
        self.assertTupleEqual((), result)

    def test_trait_affices_one(self):
        class_ = SpectralClassification('f9p')
        result = nmans.get_trait_affices(class_)
        self.assertEqual(1, len(result))

    def test_trait_affices_two(self):
        class_ = SpectralClassification('f9pw')
        result = nmans.get_trait_affices(class_)
        self.assertEqual(2, len(result))

    @patch('nmans._nmans.portmanteau')
    def test_system_name(self, mock_portmanteau: Mock):
        mock_portmanteau.get_word.return_value = 'foo'
        class_ = SpectralClassification('o0pw')
        result = nmans.get_system_name('region', class_)
        self.assertEqual(3, len(result.split('-')))

    @patch('nmans._nmans.portmanteau')
    def test_system_name_invalid(self, mock_portmanteau: Mock):
        mock_portmanteau.get_world.return_value = 'foo'
        class_ = SpectralClassification('o0z')
        self.assertRaises(
            NmansException,
            nmans.get_system_name,
            *['region', class_]
        )


if __name__ == '__main__':
    unittest.main()
