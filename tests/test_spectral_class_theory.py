import os
import unittest
from unittest.mock import Mock, patch

import nmans
from nmans.models import SpectralClass


@unittest.skipIf('NMANS_THEORY' not in os.environ.keys(), 'hypothetical')
class TestSpectralClassificationTheory(unittest.TestCase):

    @patch('nmans._nmans.portmanteaur')
    def test_system_name_multiple_traits(self, _: Mock):
        class_ = SpectralClass('o0pqpq')
        result = nmans.get_system_name('region', class_)
        self.assertEqual(5, len(result.split('-')))


if __name__ == '__main__':
    unittest.main()
