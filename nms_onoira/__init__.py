"""nms_onoira - Automate naming of discoveries in No Man's Sky"""

__all__ = [
    'get_version'
]

from typing import Tuple as __Tuple

from nms_onoira.__version__ import __author__
from nms_onoira.__version__ import __author_email__
from nms_onoira.__version__ import __license__
from nms_onoira.__version__ import __version__
from nms_onoira.__version__ import VERSION as __VERSION

from nms_onoira import models
from nms_onoira import config
from nms_onoira import exceptions

from nms_onoira._nms_onoira import get_system_name


def get_version() -> __Tuple[int]:
    return __VERSION
