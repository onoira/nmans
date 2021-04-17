# nmans

Tool to automate naming of discoveries in _No Man's Sky_ using [Odin's convention][0].

[0]: https://www.odingaming.com/2018/01/15/no-mans-sky-naming-convention/ "No Man’s Sky Naming Convention – Odin’s Convention"

## Requirements

- `click`
- `jsons (>= 1.4.2)`
- [github/onoira/portmanteaur](https://github.com/onoira/portmanteaur)

`jsonschema` is also required for schema validation.

## Usage

See `nmans --help` for more details.

Configuration is (by default) read from `~/.config/nmans/config.json`, or the `NMANS_PATH` environment variable. If the path does not exist, it will be made for you.

Empty files are ignored with the defaults (noted by a warning), and all configs can be reflowed or populated with `nmans list-config --reflow`.

## Contributing

    python3 -m pip install -e .
    ./run_tests.sh

Refer to the schema when testing configuration setups:

    python3 -m install -e ".[Validation]"
    validate.py path/to/config.json

## License

[AGPLv3](LICENSE)
