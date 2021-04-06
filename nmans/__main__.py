"""__main__ - CLI application for automating the naming of discoveries in No Man's Sky"""
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

from nmans import _cli
from nmans import config
from nmans import get_system_name
from nmans.models import SpectralClassification

@click.group()
def main(): pass


@main.command()
@click.argument('region')
@click.argument('spectral-class')
def system(region: str, spectral_class: str):
    spectral_class = spectral_class.lower()
    classification = SpectralClassification(spectral_class)
    click.echo(get_system_name(region, classification))


@main.command()
@click.option('--spectral-class', prompt=True, help='Spectral class of the host star')
@click.option('--weather')
@click.option('--sentinels')
@click.option('--fauna')
@click.option('--flora')
def planet(
    spectral_class: str,
    weather: str = str(),
    sentinels: str = str(),
    fauna: str = str(),
    flora: str = str()
):
    weather = _cli.select_weather(weather)
    sentinels = _cli.select_characteristic(sentinels, subject='sentinels')
    fauna = _cli.select_characteristic(fauna, subject='fauna')
    flora = _cli.select_characteristic(flora, subject='flora')


@main.command()
def list_config():
    _config = {
        'affices': config.TRAIT_AFFICES,
        'deities': config.SPECTRAL_NAMES,
        'headers': config.HEADERS
    }
    click.echo(_config)


if __name__ == '__main__':
    main()
