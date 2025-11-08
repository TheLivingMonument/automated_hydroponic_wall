#!/bin/bash

# This file is ran every hour with crontab to actuate the control algorithm.
PROJECT_DIR='/home/pia-polimi/Desktop/automated_hydroponic_wall'

source "$PROJECT_DIR/control_env/bin/activate"

notify-send "Running the control algorithm"

python3 "$PROJECT_DIR/programs/control.py" > "$PROJECT_DIR/error.log" 2>&1

