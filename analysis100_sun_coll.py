import rebound
import reboundx
import numpy as np
import os
import sys
import subprocess
import csv

# run with:  python3 analysis100_sun_coll.py ###_bin_files.txt

full_filename = sys.argv[1] # txt file with rebound bin file names


filename5 = "output.sun.coll.csv"
with open(filename5, 'a') as file:
        header = ["a1","e1","inc1","a2","e2","inc2","a3","e3","inc3","rel_inc1", "rel_inc2", "rel_inc3"]
        writer = csv.writer(file)
        writer.writerow(header)

with open(full_filename,'r') as f:
    bins = f.read().splitlines()
f.close()
for bin in bins:
    #print(bin)
    command = 'python3 analysis_sun_coll.py ' + bin + '&'
    #command = 'python analysis1csv.py ' + bin + ' ' + line_number + ' ' + parameter + '&'
    os.system(command)
    #print('ok')
#print('2')
#
# popenid = []
# for bin in bins:
#     #print(bin)
#     command = ['python3', './analysis1csv.py', bin, line_number, parameter]
#     # command = ['/usr/bin/python3', '--version']
#     pp = subprocess.Popen(command)
#     popenid.append(pp)
# for pp in popenid:
# 	pp.wait()
