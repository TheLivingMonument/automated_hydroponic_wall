#!/bin/bash

# This file is ran every hour with crontab to actuate the control algorithm.
PROJECT_DIR= '...'

source "$PROJECT_DIR/pia_env/bin/activate"

notify-send "Running the control algorithm"

python3 "$PROJECT_DIR/programs/control.py" > "$PROJECT_DIR/error.log" 2>&1

