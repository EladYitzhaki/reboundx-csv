#!/bin/bash

#SBATCH -J analysis_sun_coll
#SBATCH --output=job.%J.out.txt
#SBATCH --error=job.%J.err.txt
#SBATCH --partition=ph_hagai

###SBATCH --nodes=1              # Number of nodes
#SBATCH --ntasks=48             # Number of MPI ranks (spus)
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

export PYTHONFILE="analysis100_coll_eject.py"
export BINFILE="3jupiters_bin_files.txt"
export OPENBLAS_NUM_THREADS=1

python $PYTHONFILE $BINFILE
