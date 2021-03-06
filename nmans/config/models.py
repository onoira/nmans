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
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
from __future__ import annotations
from functools import lru_cache
from typing import Any, Optional, Sequence, TypeVar, Union

from dataclasses import asdict, dataclass


# ----------------------------------- Types ---------------------------------- #

_KT = TypeVar("_KT", range, Sequence[int])
_VT = TypeVar("_VT")


class RangeDict(dict[_KT, _VT]):
    """Dictionary supporting numerical ranges for keys

    Overlapping ranges are FIFO.
    """

    def __getitem__(self, k: Union[int, Any]) -> _VT:
        if isinstance(k, int):
            for key in self:
                if k in key:
                    return self[key]
            raise KeyError(k)
        else:
            return super().__getitem__(k)


# -------------------------------- Dataclasses ------------------------------- #


@dataclass
class Qualities():

    suffices: dict[str, str]
    weather: dict[str, str]


@dataclass
class Waypoints():

    @dataclass
    class WaypointCategory():

        theme: str
        prefices: dict[str, str]

    alien: Waypoints.WaypointCategory
    outpost: Waypoints.WaypointCategory
    transmission: Waypoints.WaypointCategory
    shelter: Waypoints.WaypointCategory
    beacon: Waypoints.WaypointCategory

    @classmethod
    @lru_cache(None)
    def get_options(cls) -> dict[str, str]:
        return {field: field for field in cls.__dataclass_fields__}

    def asdict(self) -> dict[str, Waypoints.WaypointCategory]:
     return {k: Waypoints.WaypointCategory(v['theme'], v['prefices']) for k,v in asdict(self).items()}


@dataclass
class Config():

    http_from: Optional[str]
    qualities: Qualities
    spectra: RangeDict[range, dict[str, str]]
    tempers: dict[str, str]
    traits: dict[str, str]
    waypoints: Optional[Waypoints]
