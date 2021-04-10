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
from __future__ import annotations

from dataclasses import dataclass
from nmans.config.exceptions import NmansConfigException
from typing import Any


# ----------------------------------- Types ---------------------------------- #

class RangeDict(dict):
    """Dictionary supporting numerical ranges for keys

    Overlapping ranges are FIFO.
    """

    @classmethod
    def from_json(cls, d: dict[str, Any]) -> RangeDict:
        rd = cls()
        for k, v in d.items():
            try:
                rd[range(*map(int, k.split(',')))] = v
            except (TypeError, ValueError) as e:
                s = {
                    TypeError: "do you have too many numbers?",
                    ValueError: "are you using numbers?"
                }[type(e)]
                raise NmansConfigException(f"invalid range '{k}': {e} ({s})")
        return rd

    def to_json(self) -> dict[str, Any]:
        d = dict()
        for k, v in self.items():
            k: range
            d[f'{k.start},{k.stop}'] = v
        return d

    def __getitem__(self, item):
        if not isinstance(item, range):
            for key in self:
                if item in key:
                    return self[key]
            raise KeyError(item)
        else:
            return super().__getitem__(item)


# -------------------------------- Dataclasses ------------------------------- #

@dataclass
class Qualities():

    suffices: dict[str, str]
    weather: dict[str, str]

    @classmethod
    def empty(cls) -> Qualities:
        return cls(dict(), dict())

    @classmethod
    def from_json(cls, d: dict[str, dict]) -> Qualities:
        if not d:
            return cls.empty()
        suffices = d.get('suffices', dict())
        weather = d.get('weather', dict())
        return cls(suffices, weather)

    def to_json(self) -> dict[str, Any]:
        d = dict()
        d['suffices'] = self.suffices
        d['weather'] = self.weather
        return d


@dataclass
class Config():

    http_from: str
    qualities: Qualities
    spectra: RangeDict[range, dict[str, str]]
    tempers: dict[str, str]
    traits: dict[str, str]

    @classmethod
    def from_json(cls, d: dict[str, Any]) -> Config:
        http_from = d.get('_http_from', '')
        qualities = Qualities.from_json(d.get('qualities', {}))
        spectra = RangeDict.from_json(d.get('spectra', {}))
        tempers = d.get('tempers', {})
        traits = d.get('traits', {})
        return cls(
            http_from,
            qualities,
            spectra,
            tempers,
            traits,
        )

    def to_json(self) -> dict[str, Any]:
        d = dict()
        d['_http_from'] = self.http_from
        d['qualities'] = self.qualities.to_json()
        d['spectra'] = self.spectra.to_json()
        d['tempers'] = self.tempers
        d['traits'] = self.traits
        return d
