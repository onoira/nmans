"""_nms_onoira - Package internals"""
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
from nms_onoira.config.deities import DEITIES
import re

from nms_onoira import portmanteau
from nms_onoira.config import AFFICES
from nms_onoira.exceptions import NmsOnoiraException
from nms_onoira.models import StarClassification

_RE_SYSTEM_CLASSIFICATION = re.compile(
    r'^[obafgkmltye][0-9][efhkmnpqsvw]{,2}$',
    re.IGNORECASE
)


def is_valid(classification: StarClassification) -> bool:
    code = str(classification)
    return _RE_SYSTEM_CLASSIFICATION.match(code)


def get_affices(classification: StarClassification) -> tuple[str]:
    if classification.oddities == str():
        return tuple()

    affices = list()
    for c in classification.oddities:
        affices.append(AFFICES[c])

    return tuple(affices)


def get_deity(classification: StarClassification) -> str:
    return DEITIES[classification.luminosity][classification.classification]


def get_system_name(region: str, classification: StarClassification) -> str:
    if not is_valid(classification):
        raise NmsOnoiraException("Invalid star class", str(classification))

    deity = get_deity(classification)
    name = portmanteau.get_word([region, deity])

    affices = get_affices(classification)
    for idx, affix in enumerate(affices):
        if idx == 0:
            name = f'{affix}-{name}'
        else:
            name = f'{name}-{affix}'

    return name
