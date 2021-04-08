## Setup

Read this first: https://github.com/Blizzard/s2client-proto#downloads

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
```
