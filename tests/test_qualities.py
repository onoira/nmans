import unittest
from unittest.mock import Mock, patch

import nmans
from nmans.config import defaults
from nmans.config.models import Config
from nmans.models import PlanetQualities


def read_config() -> Config:
    config = defaults.default_config
    config.qualities.weather = {'foo': 'bar'}
    config.qualities.suffices = {
        'dead': 'beef',
        '1bad': 'b002',
        'baad': 'f00d'
    }
    return config


@patch('nmans._nmans.config.read_config', read_config)
class TestQualities(unittest.TestCase):

    def test_qualities_translated(self) -> None:
        qualities = PlanetQualities('foo', 'dead', '1bad', 'baad')
        result = nmans.get_qualities_translated(qualities)
        self.assertEqual('bar', result.weather)
        self.assertEqual('beef', result.sentinels)
        self.assertEqual('b002', result.fauna)
        self.assertEqual('f00d', result.flora)
