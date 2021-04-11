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

from typing import Union

import json
import os
import warnings
from pathlib import Path
from functools import lru_cache

import jsons
from portmanteaur import default_headers, default_user_agent

from nmans import __name__, __version__
from nmans.config.defaults import default_config
from nmans.config.exceptions import NmansConfigWarning
from nmans.config.models import Config


def _range_deserializer(obj: list[int], cls: range, **_) -> range:
    return cls(*obj)


jsons.set_deserializer(_range_deserializer, range)


def _range_serializer(obj: range, **_) -> list[int]:
    return list((obj.start, obj.stop))


jsons.set_serializer(_range_serializer, range)


@lru_cache(None)
def _get_config_path():
    p: Path
    if p := os.environ.get('NMANS_PATH', None):
        p = os.path.expanduser(p)
    else:
        p = Path(os.environ['HOME']) / '.config' / __name__ / 'config.json'
    return p


def write_config(config: Config = None) -> None:
    if not config:
        config = read_config()
    p = _get_config_path()
    with open(p, 'w') as fp:
        fp.write(jsons.dumps(
            config,
            jdkwargs={
                'indent': 2,
                'ensure_ascii': False
            }
        ))


@lru_cache(None)
def read_config() -> Config:

    p = _get_config_path()

    config: Config
    if not os.path.exists(p):
        os.makedirs(Path(*os.path.split(p)[:-1]), exist_ok=True)
        config = default_config
        write_config(config)
    else:
        try:
            with open(p, 'r') as fp:
                config = jsons.loads(fp.read(), cls=Config)
        except (json.decoder.JSONDecodeError, jsons.DecodeError) as e:
            warnings.warn(
                f"unable to load config (falling back to defaults): {e}",
                NmansConfigWarning
            )
            config = default_config

    return config


@lru_cache(None)
def get_http_headers():
    headers = {
        **default_headers,
        'User-Agent': f'{default_user_agent} {__name__}/{__version__} '
    }
    if read_config().http_from:
        headers['From'] = read_config().http_from
    return headers
