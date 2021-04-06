"""nmans - Automate naming of discoveries in No Man's Sky"""

__all__ = [
    'get_version'
]

from nmans.__version__ import __author__
from nmans.__version__ import __author_email__
from nmans.__version__ import __license__
from nmans.__version__ import __version__
from nmans.__version__ import VERSION as __VERSION

from nmans import models
from nmans import config
from nmans import exceptions

from nmans._nmans import is_valid
from nmans._nmans import get_trait_affices
from nmans._nmans import get_spectral_name
from nmans._nmans import get_system_name


def get_version() -> tuple[int]:
    return __VERSION
