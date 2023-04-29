"""portmanfaux - Portmanteau generator

Replacement for `portmanteaur' which cannot handle non-ASCII characters.
"""
# Derived from Michael Paul's `PortManFaux' class:
# https://github.com/MickeyPvX/nms_name_gen/blob/989dc5c5be8811e79d0b307109ff35d119500846/app/pmf_gen.py
#
# Copyright (c) 2019 Michael Paul
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import random
from typing import Any, Generator

import portmanteaur

MIN_LEN = 3


def _gen_words(words: list[str]) -> Generator[str, None, None]:
    """
    Generates all possible word combinations
    """
    if len(words) != 2:
        raise ValueError(f'words: {words} is not a list with len() == 2')
    for x in range(1, len(words[0])):
        for y in range(1, len(words[1])):
            yield f'{words[0][:-x]}{words[1][y:]}'
            yield f'{words[1][:-y]}{words[0][x:]}'


def _get_word(words: list[str]) -> str:
    prospects = {i for i in _gen_words(words) if len(i) >= MIN_LEN}
    return random.choice(list(prospects))


def get_word(words: list[str], **kwargs: dict[str, Any]) -> str:
    return portmanteaur.get_word(words, **kwargs) if ''.join(words).isascii() else _get_word(words)
