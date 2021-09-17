#!/bin/bash
scp v16b915@hyalite.rci.montana.edu:/mnt/lustrefs/scratch/v16b915/lms_scan/*.mat ./data
python sort.py

