import unittest
from unittest.mock import Mock, patch

import nmans
from nmans.exceptions import NmansException
from nmans.models import PlanetaryCharacteristics, SpectralClassification


class TestPlanetaryCharacteristics(unittest.TestCase):

    @patch('nmans._nmans.portmanteaur')
    @patch('nmans._nmans.get_characteristics_translated', lambda _: PlanetaryCharacteristics.empty())
    def test_planet_name(self, mock_portmanteaur: Mock):
        class_ = SpectralClassification('o0p')
        chars_ = PlanetaryCharacteristics.empty()
        nmans.get_planet_name(class_, chars_)
        mock_portmanteaur.get_words.assert_not_called()
        mock_portmanteaur.get_word.assert_called_once()


if __name__ == '__main__':
    unittest.main()
