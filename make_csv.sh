#!/bin/bash
grep "Test MSE:" data/*_01samples_*_snr.out.txt | cut -d _ -f 3,4  | cut -b 1,2,25- > mse_01.csv
grep "Test MSE:" data/*_02samples_*_snr.out.txt | cut -d _ -f 3,4  | cut -b 1,2,25- > mse_02.csv
grep "Test MSE:" data/*_03samples_*_snr.out.txt | cut -d _ -f 3,4  | cut -b 1,2,25- > mse_03.csv
grep "Test MSE:" data/*_04samples_*_snr.out.txt | cut -d _ -f 3,4  | cut -b 1,2,25- > mse_04.csv
grep "Test MSE:" data/*_05samples_*_snr.out.txt | cut -d _ -f 3,4  | cut -b 1,2,25- > mse_05.csv
grep "Test MSE:" data/*_06samples_*_snr.out.txt | cut -d _ -f 3,4  | cut -b 1,2,25- > mse_06.csv
grep "Test MSE:" data/*_07samples_*_snr.out.txt | cut -d _ -f 3,4  | cut -b 1,2,25- > mse_07.csv
grep "Test MSE:" data/*_08samples_*_snr.out.txt | cut -d _ -f 3,4  | cut -b 1,2,25- > mse_08.csv
grep "Test MSE:" data/*_09samples_*_snr.out.txt | cut -d _ -f 3,4  | cut -b 1,2,25- > mse_09.csv
grep "Test MSE:" data/*_10samples_*_snr.out.txt | cut -d _ -f 3,4  | cut -b 1,2,25- > mse_10.csv

