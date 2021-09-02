#!/bin/bash
grep "Test MSE:" 1942769_01samples_*_snr.out.txt | cut -d _ -f 3,4  | cut -b 1,2,25- > mses.csv

