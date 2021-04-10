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

from nmans.config.models import RangeDict, Qualities, Config

default_qualities = Qualities.empty()

default_spectra = RangeDict({
    range(0, 2): {
        'o': "",
        'b': "",
        'a': "",
        'f': "",
        'g': "",
        'k': "",
        'm': "",
        'l': "",
        't': "",
        'y': "",
        'e': ""
    },
    range(2, 4): {
        'o': "",
        'b': "",
        'a': "",
        'f': "",
        'g': "",
        'k': "",
        'm': "",
        'l': "",
        't': "",
        'y': "",
        'e': ""
    },
    range(4, 6): {
        'o': "",
        'b': "",
        'a': "",
        'f': "",
        'g': "",
        'k': "",
        'm': "",
        'l': "",
        't': "",
        'y': "",
        'e': ""
    },
    range(6, 8): {
        'o': "",
        'b': "",
        'a': "",
        'f': "",
        'g': "",
        'k': "",
        'm': "",
        'l': "",
        't': "",
        'y': "",
        'e': ""
    },
    range(8, 10): {
        'o': "",
        'b': "",
        'a': "",
        'f': "",
        'g': "",
        'k': "",
        'm': "",
        'l': "",
        't': "",
        'y': "",
        'e': ""
    }
})

default_tempers = {
    'unintelligent': '',
    'migratory': '',
    'hibernator': '',
    'distinctive': '',
    'active': '',
    'erratic': '',
    'bold': '',
    'sedate': '',

    # Passive:
    'ambulatory': '',
    'amenable': '',
    'calm': '',
    'docile': '',
    'farsighted': '',
    'passive': '',
    'submissive': '',
    'unconcerned': '',
    'wise': '',
    'anxious': '',
    'cautious': '',
    'defensive': '',

    # Prey:
    'fearful': '',
    'prey': '',
    'shy': '',
    'skittish': '',
    'timid': '',

    # Predator (player):
    'aggressive': '',
    'cruel': '',
    'dangerous': '',
    'hostile': '',
    'reckless': '',
    'vicious': '',
    'violent': '',

    # Predator:
    'hunting': '',
    'predator': '',
    'stalking': '',
    'unpredictable': '',
    'volatile': ''
}

default_traits = {
    'e': '',
    'f': '',
    'h': '',
    'k': '',
    'm': '',
    'n': '',
    'p': '',
    'q': '',
    's': '',
    'v': '',
    'w': ''
}

default_config = Config(
    http_from='',
    qualities=default_qualities,
    spectra=default_spectra,
    tempers=default_tempers,
    traits=default_traits
)
