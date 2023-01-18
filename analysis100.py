import rebound
import reboundx
import numpy as np
import os
import sys

# run with:  python3 analysis100.py ###_bin_files.txt ##15 ##a

full_filename = sys.argv[1] # txt file with rebound bin file names
line_number = sys.argv[2]
parameter = sys.argv[3]

with open(full_filename,'r') as f:
    bins = f.read().splitlines()
f.close()
for bin in bins:
    #print(bin)
    command = 'python3 analysis1csv.py ' + bin + ' ' + line_number + ' ' + parameter + '&'
    os.system(command)