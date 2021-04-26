import unittest
from unittest.mock import patch

import nmans
import nmans._cli as cli
from nmans.config import defaults
from nmans.config.models import Config
from nmans.models import SpectralClass


def read_config() -> Config:
    config = defaults.default_config
    config.spectra[9]['f'] = 'arengee'
    return config


@patch('nmans._nmans.config.read_config', read_config)
class TestSpectralClass(unittest.TestCase):

    def test_spectral_name(self) -> None:
        class_ = SpectralClass('f9')
        result = nmans.get_spectral_name(class_)
        self.assertEqual('arengee', result)


class TestSpectralClassCli(unittest.TestCase):

    def test_common_class_is_valid(self) -> None:
        spectral_class = 'f9'
        result = cli.is_valid(spectral_class)
        self.assertTrue(result)

    def test_garbage_text_is_invalid(self) -> None:
        spectral_class = "!@#$%^&*()`~'"
        result = cli.is_valid(spectral_class)
        self.assertFalse(result)

    def test_class_no_substype_is_invalid(self) -> None:
        spectral_class = 'f'
        result = cli.is_valid(spectral_class)
        self.assertFalse(result)
