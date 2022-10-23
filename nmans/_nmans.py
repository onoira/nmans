"""_nmans - Package internals"""
# Copyright (C) 2021 – 2022 <onoira@psiko.zone>
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

import portmanteaur
from nmans import config
from nmans.models import PlanetQualities, SpectralClass


def get_trait_affices(class_: SpectralClass) -> tuple[str, ...]:
    affices = list()
    for trait_code in class_.traits:
        affices.append(config.read_config().traits[trait_code])
    return tuple(affices)


def get_spectral_name(class_: SpectralClass) -> str:
    return config.read_config().spectra[class_.subtype][class_.type]


def get_system_name(region: str, class_: SpectralClass) -> str:

    spectral_name = get_spectral_name(class_)
    name: str = portmanteaur.get_word(
        [region, spectral_name],
        headers=config.get_http_headers()
    )

    affices = get_trait_affices(class_)
    for idx, affix in enumerate(affices):
        if idx % 2 == 1:
            name = f'{affix}-{name}'
        else:
            name = f'{name}-{affix}'

    return name


def get_qualities_translated(qualities: PlanetQualities) -> PlanetQualities:

    qualities_t = PlanetQualities.empty()

    _weather = config.read_config().qualities.weather
    _suffices = config.read_config().qualities.suffices

    qualities_t.weather = _weather[qualities.weather]
    qualities_t.sentinels = _suffices[qualities.sentinels]
    qualities_t.fauna = _suffices[qualities.fauna]
    qualities_t.flora = _suffices[qualities.flora]

    return qualities_t


def get_planet_name(class_: SpectralClass, qualities: PlanetQualities) -> str:

    qualities_t = get_qualities_translated(qualities)
    spectral_name = get_spectral_name(class_)

    name: str = portmanteaur.get_word(
        [spectral_name, qualities_t.weather],
        headers=config.get_http_headers()
    )

    name += f'-'
    name += f'{qualities_t.sentinels}'
    name += f'{qualities_t.fauna}'
    name += f'{qualities_t.flora}'

    return name


def get_fauna_name(genus: str, temper: str, specific_name: str) -> str:

    deity = config.read_config().tempers[temper]
    name = portmanteaur.get_word(
        [deity, specific_name]
    )

    return f"{genus.title()} {name} [Planet]"


def get_waypoint_name(category: str, variant: str, theme: str) -> str:
    return f"{get_variant_translated(category, variant)}-({theme})"


def get_variant_translated(category: str, variant: str) -> str:
    return config.read_config().waypoints.asdict()[category].prefices[variant]
