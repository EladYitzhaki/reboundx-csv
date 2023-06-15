import numpy as np
import os
import csv
import sys

# need todo get time, one of m a e i and filename from user then do the rest make csv file with all the data

full_filename = sys.argv[1] # bin file
filename0 = os.path.splitext(full_filename)[0]
print(filename0)
file_number = filename0.split("_")[1]
print(file_number)
filename1 = "{0}.cart.csv".format(filename0)
filename2 = "{0}.orb.csv".format(filename0)
filename3 = "{0}.coll.csv".format(filename0)
filename4 = "{0}.eject.csv".format(filename0)

#
# with open(filename1) as f:
#     f.seek(-2, os.SEEK_END)
#     last_line = next(f)
# print(last_line)

filename5 = "output.coll.eject.csv"
filename6 = "output.coll.csv"
filename7 = "output.eject.csv"

# coll
with open(filename3, 'r') as f:
    mycsv = csv.reader(f)
    next(mycsv, None)
    for row in mycsv:
        time = row[0]
        m1 = row[1]
        m2 = row[1+8]
        m3 = row[1+16]
        coll= [time, m1, m2, m3,file_number]
        with open(filename6, 'a') as file:
            writer = csv.writer(file)
            writer.writerow(coll)
            print(coll)
    
# eject
with open(filename4, 'r') as f:
    mycsv = csv.reader(f)
    next(mycsv, None)
    for row in mycsv:
        time = row[0]
        m1 = row[1]
        eject= [time, m1,file_number]
        print(eject)

        with open(filename7, 'a') as file:
            writer = csv.writer(file)
            writer.writerow(eject)
#     
# with open(filename5, 'a') as file:
#     writer = csv.writer(file)
#     writer.writerow(coll)
#     writer.writerow(eject)
# 
# with open(filename1, 'rb') as f:
#     mycsv = csv.reader(f)
#     mycsv = list(mycsv)
#     text = mycsv[-1][2]

#     rows = list(csv.reader(f))
#     print(rows[-1][2])
#     #
#     lines = f.read().splitlines()
#     last_line= lines[-1]
#     print(last_line)
f.close()

#
# if parameter == 'coll':
#     df = pd.read_csv(filename3)
#     time =
#     del df
# if parameter == 'eject':
#     df = pd.read_csv(filename4)
#     del df
