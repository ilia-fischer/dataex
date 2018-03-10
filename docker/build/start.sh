#! /bin/bash

[ ! "$DATAEX_HOME" ] || DATAEX_HOME = "/opt/dataex"

cd $DATAEX_HOME
node server.js