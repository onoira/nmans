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
import click
import nmans.config as config


_T_WORDMAP = dict[str, str]
_T_OPTIONS = tuple[_T_WORDMAP, _T_WORDMAP]


def _build_options(d): return dict([(str(idx), k)
                                    for idx, (k, v) in enumerate(d.items()) if v])


def _select_option(
    option: str,
    options: _T_OPTIONS,
    prompt: str,
    expose_options: bool
) -> str:

    _options, _names = options

    def _validate_option() -> str:
        if not option:
            return str()
        if option.isdigit() and option in _options.keys():
            return _options[option]
        elif option in _names.keys():
            return option
        else:
            click.echo(f'Invalid {prompt}')
            return str()

    option_valid = False
    while not option_valid:
        if expose_options:
            click.echo()
            for k, v in _options.items():
                s = f'[{k}] {v}'
                name = _names.get(v, '')
                s += f' ({name})' if name else ''
                click.echo(s)
            click.echo()
            expose_options = False

        if not option:
            option = click.prompt(f'{prompt.title()} (?)')
        else:
            # This is only possible on first entry.
            expose_options = True

        if option == '?':
            expose_options = True
            option = ''

        option_valid = bool(option := _validate_option())

    return option


def is_valid(spectral_class: str) -> bool:
    re_spectral_class = re.compile(
        r'^[obafgkmltye][0-9][efhkmnpqsvw]{,2}$',
        re.IGNORECASE
    )
    return re_spectral_class.match(spectral_class)


def select_quality(option: str, subject: str) -> str:
    options = _build_options(config.read_config().qualities.suffices)
    return _select_option(
        option,
        options=(options, config.read_config().qualities.suffices),
        prompt=subject,
        expose_options=False
    )


def select_weather(option: str) -> str:
    options = _build_options(config.read_config().qualities.weather)
    return _select_option(
        option,
        options=(options, config.read_config().qualities.weather),
        prompt='weather',
        expose_options=False
    )


def select_habitat(option: str) -> str:
    options = dict([(str(idx), k)
                    for idx, k in enumerate(config.const.GENERA.keys())])
    return _select_option(
        option,
        options=(options, dict((v, None) for _,v in options.items())),
        prompt='habitat',
        expose_options=not option
    )


def select_genus(option: str, category: str) -> str:
    options = _build_options(config.const.GENERA[category])
    return _select_option(
        option,
        options=(options, config.const.GENERA[category]),
        prompt='genus',
        expose_options=False
    )


def select_temper(option: str) -> str:
    options = _build_options(config.read_config().tempers)
    return _select_option(
        option,
        options=(options, config.read_config().tempers),
        prompt='temper',
        expose_options=False
    )
