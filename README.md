# All Your Base Bot

This is a StarCraft II Bot.

* Proof of concept.
* Work in progress.
* Does actually beat a medium difficulty Protoss AI.

## Setup

Read this first: https://github.com/Blizzard/s2client-proto#downloads

Have StarCraft II installed. On a Mac, it is typically in `/Applications/StarCraft II/`.

Download map packs and `iagreetotheeula`.

``` bash

export MAPSDIR=/Applications/StarCraft\ II/Maps

mkdir map_packs
cd map_packs
wget http://blzdistsc2-a.akamaihd.net/MapPacks/Ladder2017Season1.zip
wget http://blzdistsc2-a.akamaihd.net/MapPacks/Ladder2017Season2.zip
wget http://blzdistsc2-a.akamaihd.net/MapPacks/Ladder2017Season3_Updated.zip
wget http://blzdistsc2-a.akamaihd.net/MapPacks/Ladder2017Season4.zip
wget http://blzdistsc2-a.akamaihd.net/MapPacks/Ladder2018Season1.zip
wget http://blzdistsc2-a.akamaihd.net/MapPacks/Ladder2018Season2_updated.zip
wget http://blzdistsc2-a.akamaihd.net/MapPacks/Ladder2018Season3.zip
wget http://blzdistsc2-a.akamaihd.net/MapPacks/Ladder2018Season4.zip
wget http://blzdistsc2-a.akamaihd.net/MapPacks/Ladder2019Season1.zip
wget http://blzdistsc2-a.akamaihd.net/MapPacks/Ladder2019Season2.zip
wget http://blzdistsc2-a.akamaihd.net/MapPacks/Ladder2019Season3.zip
wget http://blzdistsc2-a.akamaihd.net/MapPacks/Melee.zip

unzip -P iagreetotheeula ./Ladder2017Season1.zip -d $MAPSDIR
unzip -P iagreetotheeula ./Ladder2017Season2.zip -d $MAPSDIR
unzip -P iagreetotheeula ./Ladder2017Season3_Updated.zip -d $MAPSDIR
unzip -P iagreetotheeula ./Ladder2017Season4.zip -d $MAPSDIR
unzip -P iagreetotheeula ./Ladder2018Season1.zip -d $MAPSDIR
unzip -P iagreetotheeula ./Ladder2018Season2_updated.zip -d $MAPSDIR
unzip -P iagreetotheeula ./Ladder2018Season3.zip -d $MAPSDIR
unzip -P iagreetotheeula ./Ladder2018Season4.zip -d $MAPSDIR
unzip -P iagreetotheeula ./Ladder2019Season1.zip -d $MAPSDIR
unzip -P iagreetotheeula ./Ladder2019Season2.zip -d $MAPSDIR
unzip -P iagreetotheeula ./Ladder2019Season3.zip -d $MAPSDIR
unzip -P iagreetotheeula ./Melee.zip -d $MAPSDIR

cd ..
```

Run POC::

``` bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python main.py
```
