# F-Droid

Selection of FOSS Android apps on F-Droid

## Overviews

The overviews are:
- [English overview](overview-en.md)
- [Dutch overview](overview-nl.md)
- [Spanish overview](overview-es.md)

## Build

To build the overviews, install

```sh
sudo apt-get -y install python3-pip python3-venv
python3 -m venv .venv
. .venv/bin/activate
pip install -Ur requirements.txt
```

and then run `./build.sh`.

## TODO

https://get.alternative.to/

spotube

comaps (setting)

signal

firefox plugins

https://f-droid.org/en/packages/com.vladpen.cams/

https://github.com/LukeStonehm/LogicalDefence/issues/79
https://f-droid.org/en/packages/za.co.lukestonehm.logicaldefence/

## Development

Install

```sh
. .venv/bin/activate
pip install -Ur requirements-dev.txt
```

Run the linters with `./lint.sh`.

