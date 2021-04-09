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

import portmanteaur

from nmans import config
from nmans.models import PlanetaryCharacteristics, SpectralClassification

_RE_SYSTEM_CLASSIFICATION = re.compile(
    r'^[obafgkmltye][0-9][efhkmnpqsvw]{,2}$',
    re.IGNORECASE
)


def is_valid(classification_code: str) -> bool:
    return _RE_SYSTEM_CLASSIFICATION.match(classification_code)


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

    spectral_name = get_spectral_name(classification)
    name = portmanteaur.get_word(
        [region, spectral_name],
        headers=config.get_http_headers()
    )

    affices = get_trait_affices(classification)
    for idx, affix in enumerate(affices):
        if idx % 2 == 1:
            name = f'{affix}-{name}'
        else:
            name = f'{name}-{affix}'

    return name


def get_characteristics_translated(
    characteristics: PlanetaryCharacteristics
) -> PlanetaryCharacteristics:

    characteristics_translated = PlanetaryCharacteristics.empty()

    characteristics_translated.weather = WEATHER_NAMES[characteristics.weather]
    characteristics_translated.sentinels = CHARACTERISTIC_SUFFICES[characteristics.sentinels]
    characteristics_translated.fauna = CHARACTERISTIC_SUFFICES[characteristics.fauna]
    characteristics_translated.flora = CHARACTERISTIC_SUFFICES[characteristics.flora]

    return characteristics_translated


def get_planet_name(
    system_classification: SpectralClassification,
    characteristics: PlanetaryCharacteristics
) -> str:

    # Maybe we're just tired, but all the code for planets is pretty ugly so far.
    characteristics_translated = get_characteristics_translated(
        characteristics)
    spectral_name = get_spectral_name(system_classification)

    name = portmanteaur.get_word(
        [spectral_name, characteristics_translated.weather],
        headers=config.get_http_headers()
    )

    # Apply suffix
    name += f'-'
    name += f'{characteristics_translated.sentinels}'
    name += f'{characteristics_translated.fauna}'
    name += f'{characteristics_translated.flora}'

    return name
