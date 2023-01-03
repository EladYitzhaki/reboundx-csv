#!/bin/bash

#SBATCH -J first_try_3jupiter
#SBATCH --output=job.%J.out.txt
#SBATCH --error=job.%J.err.txt
#SBATCH --partition=ph_hagai

###SBATCH --nodes=1              # Number of nodes
#SBATCH --ntasks=10             # Number of MPI ranks (spus)
###SBATCH --ntasks-per-node=96 # Number of MPI ranks (cpus) per node
###SBATCH --ntasks-per-socket=1  # Number of tasks per processor socket on the node
#SBATCH --cpus-per-task=2      # Number of OpenMP threads for each MPI process/rank
###SBATCH --exclude=nyx-wn001.nyx,nyx-wn002.nyx,nyx-wn003.nyx,nyx-wn004.nyx,nyx-wn005.nyx

###SBATCH --mail-type=ALL
###SBATCH --mail-user=hilaglanz@gmail.com

#SBATCH --time=14-00 #14 days


###SBATCH --mem=500G
###SBATCH --mem-per-cpu=40G
source /usr/local/ph_hagai/anaconda3/bin/activate rebound-env

export PYTHONFILE="read_bin_file_and_and_run.py"
export BINFILE="3jupiters0.bin"

python $PYTHONFILE BINFILE
