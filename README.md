# reboundx-simulation-creator-and-running

This is an python extantion of the N-body code rebound and reboundx
They have an API of those codes: https://rebound.readthedocs.io/en/latest/api/
https://reboundx.readthedocs.io/en/latest/

It create a rebound simulasion by running the file of the initial conditions, and save randomiedes versions of them in bin files.
Then you can run the simulation on those bin files by using the python codes with weak tides or without them.

The output is to csv files: cartision coordinate of all bodies, orbital elements- not for the main star, collision, ejection. cart,orb,coll,eject.

