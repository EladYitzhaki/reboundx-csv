import rebound
import reboundx
import numpy as np
import os
import sys

full_filename = sys.argv[1] # txt file with rebound bin file names
with open(full_filename,'r') as f:
    bins = f.read().splitlines()
f.close()
for bin in bins:
    #print(bin)
    command = 'python3 read_bin_file_and_run.py ' + bin + '&'
    os.system(command)
