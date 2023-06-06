import numpy as np
import os
import csv
import sys
import pandas as pd

# need todo get time, one of m a e i and filename from user then do the rest make csv file with all the data

def relative_inc(i1,i2,Omega1,Omega2):
    return np.arccos(np.cos(i1)*np.cos(i2)+np.sin(i1)*np.sin(i2)*np.cos(Omega1-Omega2))

full_filename = sys.argv[1] # bin file
filename0 = os.path.splitext(full_filename)[0]
# print(filename0)
filename1 = "{0}.cart.csv".format(filename0)
filename2 = "{0}.orb.csv".format(filename0)
filename3 = "{0}.coll.csv".format(filename0)
filename4 = "{0}.eject.csv".format(filename0)

#
# with open(filename1) as f:
#     f.seek(-2, os.SEEK_END)
#     last_line = next(f)
# print(last_line)

filename5 = "output.sun.coll.csv"
# coll
with open(filename3, 'r') as f:
    mycsv = csv.reader(f)
    next(mycsv, None)
    for row in mycsv:
        time = row[0]
        m1 = row[1]
        m2 = row[1+8]
        m3 = row[1+16]
        hash1= row[2]
        hash2= row[2+8]

        coll= [time, m1, m2, m3]

        if float(m3) >= 1:
            if float(m2) < 1:
                hash_coll= hash2
            else:
                hash_coll= hash1

            sun_coll = []
            time_before = int(np.floor(float(time)/100))

            # find who collided with sun
            data_frame= pd.read_csv(filename1)
            for element in range(len(data_frame.columns)):
                num = (element - 1)
                if num % 8 == 2:
                    hash_cand = float(df.iat[time_before, element])
                if hash_cand == hash_coll
                    planet_coll_num = np.floor(element/8)

            del data_frame

            df = pd.read_csv(filename2)

            a = float(df.iat[time_before, 1 + 6*planet_coll_num])
            e = float(df.iat[time_before, 2+6*planet_coll_num])
            inc = float(df.iat[time_before, 3+6*planet_coll_num])
            Omega = float(df.iat[time_before, 4+6*planet_coll_num])
            sun_coll =[a, e, inc]

            # a1 = float(df.iat[time_before, 1])
            # e1 = float(df.iat[time_before, 2])
            # inc1 = float(df.iat[time_before, 3])
            # Omega1 = float(df.iat[time_before, 4])
            # a2 = float(df.iat[time_before, 1+6])
            # e2 = float(df.iat[time_before, 2+6])
            # inc2 = float(df.iat[time_before, 3+6])
            # Omega2 = float(df.iat[time_before, 4+6])
            # a3 = float(df.iat[time_before, 1+12])
            # e3 = float(df.iat[time_before, 2+12])
            # inc3 = float(df.iat[time_before, 3+12])
            # Omega3 = float(df.iat[time_before, 4+12])
            # sun_coll = [a1, e1, inc1, a2, e2, inc2, a3, e3, inc3]
            # if np.isnan(a2):
            #     continue
            # elif np.isnan(a3):
            #     rel_inc1 = relative_inc(inc1,inc2,Omega1,Omega2)
            #     sun_coll.append(rel_inc1)
            # else:
            #     rel_inc1 = relative_inc(inc1,inc2,Omega1,Omega2)
            #     rel_inc2 = relative_inc(inc2,inc3,Omega2,Omega3)
            #     rel_inc3 = relative_inc(inc1,inc3,Omega1,Omega3)
            #     sun_coll.append(rel_inc1)
            #     sun_coll.append(rel_inc2)
            #     sun_coll.append(rel_inc3)
            # #sun_coll =[] #a e i rel inc
            with open(filename5, 'a') as file:
                writer = csv.writer(file)
                writer.writerow(sun_coll)
            del df

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
