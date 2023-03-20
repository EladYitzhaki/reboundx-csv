import rebound
import reboundx
import numpy as np
import os
import sys
import subprocess

full_filename = sys.argv[1] # txt file with rebound bin file names
with open(full_filename,'r') as f:
    bins = f.read().splitlines()
f.close()
popenid = []
for bin in bins:
    #print(bin)
    
    command = ['python3', './run_with_perturber.py', bin] 
    #command = ['python3', './read_bin_file_and_run.py', bin] 
    # command = ['/usr/bin/python3', '--version']
    pp = subprocess.Popen(command)
    popenid.append(pp)
for pp in popenid:
	pp.wait()
