"""_cli - CLI helpers"""
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
from pprint import PrettyPrinter

import click
import jsons

import nmans.config as config


_T_WORDMAP = dict[str, str]
_T_OPTIONS = tuple[_T_WORDMAP, _T_WORDMAP]

_SUFFIX_OPTIONS = dict(
    [(str(idx), i[0]) for idx, i in enumerate(
        config.read_config().qualities.suffices.items()) if i[1]]
)
_WEATHER_OPTIONS = dict(
    [(str(idx), k) for idx, (k, v) in enumerate(
        config.read_config().qualities.weather.items()) if v]
)

_re_spectral_class = re.compile(
    r'^[obafgkmltye][0-9][efhkmnpqsvw]{,2}$',
    re.IGNORECASE
)


def _validate_option(option: str, options: _T_OPTIONS, prompt: str) -> str:

    _options, _names = options
    if option.isdigit() and option in _options.keys():
        return _options[option]
    elif option in _names.keys():
        return option
    else:
        click.echo(f'Invalid {prompt} option')
        return _select_option(None, options, prompt, expose_options=True)


def is_valid(spectral_class: str) -> bool:
    return _re_spectral_class.match(spectral_class)


def _select_option(
    option: str,
    options: _T_OPTIONS,
    prompt: str,
    expose_options: bool
) -> str:

    _options, _ = options

    if expose_options:
        click.echo()
        for k, v in _options.items():
            click.echo(f'[{k}] {v}')
        click.echo()

    if not option:
        option: str = click.prompt(f'{prompt.title()} (?)')

    if option == '?':
        return _select_option(None, options, prompt, expose_options=True)

    return _validate_option(option, options, prompt)


def select_quality(option: str, subject: str):
    return _select_option(
        option,
        options=(_SUFFIX_OPTIONS, config.read_config().qualities.suffices),
        prompt=subject,
        expose_options=False
    )


def select_weather(option: str):
    return _select_option(
        option,
        options=(_WEATHER_OPTIONS, config.read_config().qualities.weather),
        prompt='weather',
        expose_options=False
    )
