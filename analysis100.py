import rebound
import reboundx
import numpy as np
import os
import sys
import subprocess
import csv

# run with:  python3 analysis100.py ###_bin_files.txt ##15 ##a
# print('100')
full_filename = sys.argv[1] # txt file with rebound bin file names
line_number = sys.argv[2]
parameter = sys.argv[3]

filename5 = "output.{0}.time{1}.csv".format(parameter, int(line_number)*100)
with open(filename5, 'a') as file:
    if parameter == 'm':
        writer = csv.writer(file)
        header = ["mass"]
        writer.writerow(header)
    if parameter == 'a':
        writer = csv.writer(file)
        header = ["a"]
        writer.writerow(header)
    if parameter == 'e':
        writer = csv.writer(file)
        header = ["e"]
        writer.writerow(header)
    if parameter == 'inc':
        writer = csv.writer(file)
        header = ["inc"]
        writer.writerow(header)
    if parameter == 'aei':
        writer = csv.writer(file)
        header = ["a","e","inc"]
        writer.writerow(header)

with open(full_filename,'r') as f:
    bins = f.read().splitlines()
f.close()
# for bin in bins:
#     #print(bin)
#     command = 'python3 analysis1csv.py ' + bin + ' ' + line_number + ' ' + parameter + '&'
#     #command = 'python analysis1csv.py ' + bin + ' ' + line_number + ' ' + parameter + '&'
#     os.system(command)
#     print('ok')
# print('2')

popenid = []
for bin in bins:
    #print(bin)
    command = ['python3', './analysis1csv.py', bin, line_number, parameter]
    # command = ['/usr/bin/python3', '--version']
    pp = subprocess.Popen(command)
    popenid.append(pp)
for pp in popenid:
	pp.wait()
