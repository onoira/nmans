"""__main__ - CLI application for automating the naming of discoveries in No Man's Sky"""
# Copyright (C) 2021 – 2022 <onoira@psiko.zone>
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

import pprint
import sys

import click
import jsons

import nmans.config as config
import nmans._cli as _cli
from nmans import get_system_name, get_planet_name, get_fauna_name, get_waypoint_name
from nmans.models import PlanetQualities, SpectralClass


@click.group()
def main() -> None: pass


@main.command()
@click.argument('region')
@click.argument('spectral-class')
def system(region: str, spectral_class: str) -> None:

    spectral_class = spectral_class.lower()
    if not _cli.is_valid(spectral_class):
        click.echo("Invalid spectral class")
        sys.exit(1)

    class_ = SpectralClass(spectral_class)
    click.echo(get_system_name(region, class_))


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
) -> None:

    spectral_class = spectral_class.lower()
    if not _cli.is_valid(spectral_class):
        click.echo("Invalid spectral class")
        sys.exit(1)

    weather = _cli.select_weather(weather)
    sentinels = _cli.select_quality(sentinels, subject='sentinels')
    fauna = _cli.select_quality(fauna, subject='fauna')
    flora = _cli.select_quality(flora, subject='flora')

    class_ = SpectralClass(spectral_class)
    qualities = PlanetQualities(
        weather,
        sentinels,
        fauna,
        flora
    )

    click.echo()
    click.echo(get_planet_name(class_, qualities))


@main.command()
@click.option('--specific-name', prompt=True, help='Original species name (NOT genus)')
@click.option('--habitat')
@click.option('--genus')
@click.option('--temper')
def fauna(
    specific_name: str,
    habitat: str = str(),
    genus: str = str(),
    temper: str = str()
) -> None:

    if not specific_name:
        click.echo("Invalid specific name")
        sys.exit(1)

    specific_name = specific_name.lower()
    habitat = _cli.select_habitat(habitat)
    genus = _cli.select_genus(genus, habitat)
    temper = _cli.select_temper(temper)

    click.echo(get_fauna_name(genus, temper, specific_name))


@main.command()
@click.option('--category')
@click.option('--variant')
def waypoint(
    category: str = str(),
    variant: str = str()
) -> None:

    if config.read_config().waypoints is None:
        raise click.ClickException("No waypoints defined in config.")

    category = _cli.select_waypoint_category(category)
    variant, theme = _cli.select_waypoint_variant(variant, category)

    click.echo(get_waypoint_name(category, variant, theme))


@main.command()
@click.option('--reflow', is_flag=True)
@click.option('--default', is_flag=True)
def list_config(reflow: bool = False, default: bool = False) -> None:
    if reflow:
        config.write_config()
    if default:
        import nmans.config.defaults as config_defaults
        _config = config_defaults.default_config
    else:
        _config = config.read_config()
    click.echo(pprint.pformat(
        jsons.dump(_config),
        sort_dicts=False
    ))


if __name__ == '__main__':
    main()
