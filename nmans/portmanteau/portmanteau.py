"""portmanteau - Generate portmanteau for name generation"""
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
# along with this program.  If not, see <https://www.gnu.org/licenses/

import random

try:
    import html5lib
except ImportError:
    raise ImportError('html5lib is required')

from requests import request
from bs4 import BeautifulSoup

from nmans.config import HEADERS

BASE_URL = 'https://www.portmanteaur.com/'
RESULTS_TRANSLATION = str.maketrans({'\n': '', ' ': ''})


def get_words(words: list[str]) -> list[str]:
    """Return all unique words from `BASE_URL`"""

    response = request(
        'GET', f'{BASE_URL}?words={"+".join(words)}',
        headers=HEADERS
    )

    cup = BeautifulSoup(response.content, 'html5lib')
    # Number of result groups is {n}*{n-1}.
    results = cup.find_all('div', {"class": 'results'})

    words = list()
    for result in results:
        result_clean = result.text.translate(RESULTS_TRANSLATION).strip()
        words.extend(result_clean.split(','))

    return list(set(words))


def get_word(words: list[str]) -> str:
    """Select a random word from `BASE_URL`"""
    words = get_words(words)
    return random.choice(words)
