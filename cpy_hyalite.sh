#!/bin/bash
rsync -P v16b915@hyalite.rci.montana.edu:/mnt/lustrefs/scratch/v16b915/lms_scan/*.mat ./data/lms
rsync -P v16b915@hyalite.rci.montana.edu:/mnt/lustrefs/scratch/v16b915/dfe_scan/*.mat ./data/dfe

