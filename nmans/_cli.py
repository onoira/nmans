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
import click

from nmans.config import CHARACTERISTIC_SUFFICES, WEATHER_NAMES

_T_WORDMAP = dict[str, str]
_T_OPTIONS = tuple[_T_WORDMAP, _T_WORDMAP]

_CHARACTERISTIC_OPTIONS = dict(
    [(str(idx), i) for idx, i in enumerate(CHARACTERISTIC_SUFFICES)]
)
_WEATHER_OPTIONS = dict(
    [(str(idx), i) for idx, i in enumerate(WEATHER_NAMES)]
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


def _select_option(
    option: str,
    options: _T_OPTIONS,
    prompt: str,
    expose_options: bool
) -> str:

    _options, _ = options

    if expose_options:
        for k, v in _options.items():
            click.echo(f'[{k}] {v}')
        click.echo()

    if not option:
        option: str = click.prompt(f'{prompt.title()} (?)')

    if option == '?':
        return _select_option(None, options, prompt, expose_options=True)

    return _validate_option(option, options, prompt)


def select_characteristic(option: str, subject: str):
    return _select_option(
        option,
        options=(_CHARACTERISTIC_OPTIONS, CHARACTERISTIC_SUFFICES),
        prompt=subject,
        expose_options=False
    )


def select_weather(option: str):
    return _select_option(
        option,
        options=(_WEATHER_OPTIONS, WEATHER_NAMES),
        prompt='weather',
        expose_options=False
    )
