"""nmans - Automate naming of discoveries in No Man's Sky"""

__all__ = [
    '__author__',
    '__author_email__',
    '__license__',
    '__version__',
    'get_version',
    'models',
    'config',
    'exceptions',
    'get_trait_affices',
    'get_spectral_name',
    'get_qualities_translated',
    'get_system_name',
    'get_planet_name',
    'get_fauna_name',
    'get_waypoint_name'
]

from nmans.__version__ import __author__
from nmans.__version__ import __author_email__
from nmans.__version__ import __license__
from nmans.__version__ import __version__
from nmans.__version__ import VERSION as __VERSION

from nmans import models
from nmans import config
from nmans import exceptions

from nmans._nmans import get_trait_affices
from nmans._nmans import get_spectral_name
from nmans._nmans import get_qualities_translated
from nmans._nmans import get_system_name
from nmans._nmans import get_planet_name
from nmans._nmans import get_fauna_name
from nmans._nmans import get_waypoint_name


def get_version() -> tuple[int, int, int]:
    return __VERSION
