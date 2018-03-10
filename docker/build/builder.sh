#! /bin/bash

#create a build directory
rm -rf dataex
mkdir -p dataex

#prepare image content
cp -r ../../api dataex
cp -r ../../basic-network dataex
cp -r ../../chaincode dataex
cp -r ../../scripts dataex
cp ../../package.json dataex
cp ../../server.js dataex

docker build .