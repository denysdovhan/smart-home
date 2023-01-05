#!/usr/bin/env bash

export SMART_HOME_DIR="$HOME/smart-home"
export PATH="$PATH:$SMART_HOME_DIR/bin"

echo "Restarting via script"
smart-home restart
