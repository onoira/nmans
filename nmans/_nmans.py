"""_nmans - Package internals"""
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
import re

from nmans import portmanteau
from nmans.config import SPECTRAL_NAMES, TRAIT_AFFICES
from nmans.exceptions import NmansException
from nmans.models import SpectralClassification

_RE_SYSTEM_CLASSIFICATION = re.compile(
    r'^[obafgkmltye][0-9][efhkmnpqsvw]{,2}$',
    re.IGNORECASE
)


def is_valid(classification: SpectralClassification) -> bool:
    code = str(classification)
    return _RE_SYSTEM_CLASSIFICATION.match(code)


def get_trait_affices(classification: SpectralClassification) -> tuple[str]:
    if classification.traits == str():
        return tuple()

    affices = list()
    for c in classification.traits:
        affices.append(TRAIT_AFFICES[c])

    return tuple(affices)


def get_spectral_name(classification: SpectralClassification) -> str:
    return SPECTRAL_NAMES[classification.spectral_subtype][classification.spectral_type]


def get_system_name(region: str, classification: SpectralClassification) -> str:
    if not is_valid(classification):
        raise NmansException("Invalid spectral class", str(classification))

    spectral_name = get_spectral_name(classification)
    name = portmanteau.get_word([region, spectral_name])

    affices = get_trait_affices(classification)
    for idx, affix in enumerate(affices):
        if idx % 2 == 1:
            name = f'{affix}-{name}'
        else:
            name = f'{name}-{affix}'

    return name
