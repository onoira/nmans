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

from nms_onoira import config
from nms_onoira import get_system_name
from nms_onoira.models import SpectralClassification


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
def list_config():
    _config = {
        'affices': config.TRAIT_AFFICES,
        'deities': config.SPECTRAL_NAMES,
        'headers': config.HEADERS
    }
    click.echo(_config)


if __name__ == '__main__':
    main()
