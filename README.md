# reboundx-simulation-creator-and-running

This is an python extantion of the N-body code rebound and reboundx
They have an API of those codes: https://rebound.readthedocs.io/en/latest/api/
https://reboundx.readthedocs.io/en/latest/

For example in the terminal run:
python3 generate_random_jupiter_bin.py

It create a rebound simulasion by running the file of the initial conditions, and save randomiedes versions of them in bin files.

Then you can run the simulation on those bin files by using the python codes with weak tides or without them.
python3 read_bin_file_and_run.py 3jupiters0.bin

The output is to csv files: cartision coordinate of all bodies, orbital elements- not for the main star, collision, ejection. cart,orb,coll,eject.

using python3 with pakeges: rebound reboundx numpy pandas
