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


class RangeDict(dict):
    def __getitem__(self, item):
        if not isinstance(item, range):
            for key in self:
                if item in key:
                    return self[key]
            raise KeyError(item)
        else:
            return super().__getitem__(item)


class StarClassification:

    def __init__(self, star_class: str):
        self.classification: str = star_class[0]
        self.luminosity: int = int(star_class[1])
        self.oddities: str
        if len(star_class) > 2:
            self.oddities = star_class[2:]
        else:
            self.oddities = str()

    def __str__(self):
        return f'{self.classification}{self.luminosity}{self.oddities}'
