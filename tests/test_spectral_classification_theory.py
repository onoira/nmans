import re
import unittest
from unittest.mock import Mock, patch

import nmans
from nmans.models import SpectralClassification


class TestSpectralClassificationTheory(unittest.TestCase):

    @patch(
        'nmans._nmans._RE_SYSTEM_CLASSIFICATION',
        re.compile(
            r'^[obafgkmltye][0-9][efhkmnpqsvw]*$',
            re.IGNORECASE
        )
    )
    @patch('nmans._nmans.portmanteaur')
    def test_system_name_multiple_traits(self, _:Mock):
        class_ = SpectralClassification('o0pqpq')
        result = nmans.get_system_name('region', class_)
        self.assertEqual(5, len(result.split('-')))


if __name__ == '__main__':
    unittest.main()
