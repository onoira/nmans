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
from typing import Optional

from dataclasses import dataclass


# ----------------------------------- Types ---------------------------------- #

class RangeDict(dict):
    """Dictionary supporting numerical ranges for keys

    Overlapping ranges are FIFO.
    """

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


@dataclass
class Config():

    http_from: Optional[str]
    qualities: Qualities
    spectra: RangeDict[range, dict[str, str]]
    tempers: dict[str, str]
    traits: dict[str, str]
