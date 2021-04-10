"""models - Package classes"""
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
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


class PlanetQualities:

    @classmethod
    def empty(_):
        return PlanetQualities('', '', '', '')

    def __init__(self, weather: str, sentinels: str, fauna: str, flora: str):
        self.weather: str = weather
        self.sentinels: str = sentinels
        self.fauna: str = fauna
        self.flora: str = flora


class SpectralClass:

    def __init__(self, spectral_class: str):
        self.type: str = spectral_class[0]
        self.subtype: int = int(spectral_class[1])
        self.traits: str
        if len(spectral_class) > 2:
            self.traits = spectral_class[2:]
        else:
            self.traits = str()

    def __str__(self):
        return f'{self.type}{self.subtype}{self.traits}'
