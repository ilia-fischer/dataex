#! /bin/bash

cd ..
tar -cvf dataex.tar dataex/scripts/*.js dataex/chaincode/ dataex/api/
scp dataex.tar mykrazylabs@35.229.120.209:.
cd dataex
