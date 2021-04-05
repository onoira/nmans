"""nms_onoira - Automate naming of discoveries in No Man's Sky"""
# Copyright (C) 2021 <onoira@psiko.zone>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>

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
#from mypackage._mypackage import my_function


def get_version() -> __Tuple[int]:
    return __VERSION
