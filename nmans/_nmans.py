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
from nmans.models import PlanetTraits, SpectralClass


def get_trait_affices(class_: SpectralClass) -> tuple[str]:
    if class_.traits == str():
        return tuple()

    affices = list()
    for trait_code in class_.traits:
        affices.append(config.read_config().traits[trait_code])

    return tuple(affices)


def get_spectral_name(class_: SpectralClass) -> str:
    return config.read_config().spectra[class_.subtype][class_.type]


def get_system_name(region: str, classification: SpectralClass) -> str:

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


# def get_characteristics_translated(
#     characteristics: PlanetTraits
# ) -> PlanetTraits:

#     characteristics_translated = PlanetTraits.empty()

#     characteristics_translated.weather = WEATHER_NAMES[characteristics.weather]
#     characteristics_translated.sentinels = CHARACTERISTIC_SUFFICES[characteristics.sentinels]
#     characteristics_translated.fauna = CHARACTERISTIC_SUFFICES[characteristics.fauna]
#     characteristics_translated.flora = CHARACTERISTIC_SUFFICES[characteristics.flora]

#     return characteristics_translated


# def get_planet_name(
#     system_classification: SpectralClass,
#     characteristics: PlanetTraits
# ) -> str:

#     # Maybe we're just tired, but all the code for planets is pretty ugly so far.
#     characteristics_translated = get_characteristics_translated(
#         characteristics)
#     spectral_name = get_spectral_name(system_classification)

#     name = portmanteaur.get_word(
#         [spectral_name, characteristics_translated.weather],
#         headers=config.get_http_headers()
#     )

#     # Apply suffix
#     name += f'-'
#     name += f'{characteristics_translated.sentinels}'
#     name += f'{characteristics_translated.fauna}'
#     name += f'{characteristics_translated.flora}'

#     return name
