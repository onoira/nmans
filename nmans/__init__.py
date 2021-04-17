"""nmans - Automate naming of discoveries in No Man's Sky"""

__all__ = [
    'get_version',
    'models',
    'config',
    'exceptions',
    'get_system_name',
    'get_planet_name',
    'get_fauna_name',
]

from nmans.__version__ import __author__
from nmans.__version__ import __author_email__
from nmans.__version__ import __license__
from nmans.__version__ import __version__
from nmans.__version__ import VERSION as __VERSION

from nmans import models
from nmans import config
from nmans import exceptions

from nmans._nmans import get_system_name
from nmans._nmans import get_planet_name
from nmans._nmans import get_fauna_name


def get_version() -> tuple[int]:
    return __VERSION
