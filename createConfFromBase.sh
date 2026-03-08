#!/bin/sh

# Oopsy doopsy i nuked all configs
# So this script rewrite them from the default base config

set -euo

createConfig(){
	cat base/server.conf | sed -e "s/\(__IP__=\)\"0.0.0.0\"/\1\"172.16.1.13\"/g" -e "s/\(__PORT__=\"\)27015\"/\1$(\awk "BEGIN {x=$1*100; print x+27015}" )\"/g" -e "s/# \(USE_RCON=\"-usercon\"\)/\1/g" -e "s/# \(__RCON_PASS__=\"\)correcthorsebatterystaple\"/\1gamebanana\"/g"
}

for i in $(seq 9); do
	createConfig $i > "inst-server$i/server.conf"
done
for i in $(seq -w 10 16); do
	createConfig $i > "inst-server$i/server.conf"
done

