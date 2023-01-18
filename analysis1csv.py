import numpy as np
import os
import csv
import sys
import pandas as pd

#line_number = 15 # give the time of 1500 years
#parameter = 'e' # m a e inc

# need todo get time, one of m a e i and filename from user then do the rest make csv file with all the data
line_number = int(sys.argv[2])
parameter = sys.argv[3]
full_filename = sys.argv[1] # bin file
filename0 = os.path.splitext(full_filename)[0]
print(filename0)
filename1 = "{0}.cart.csv".format(filename0)
filename2 = "{0}.orb.csv".format(filename0)

# #num of rows (len(df)) without header
# #num of cols (len(df.columns))

filename5 = "output.{0}.time{1}.csv".format(parameter,line_number*100)

if parameter == 'm':
    df = pd.read_csv(filename1)
    planet = 0
    for element in range(len(df.columns)):
        num = (element - 1)
        if num % 6 == 0:
            with open(filename5, 'a') as file:
                writer = csv.writer(file)
                data_point = [df.iat[line_number, element]]
                writer.writerow(data_point)
            planet += 1
if parameter == 'a':
    df = pd.read_csv(filename2)
    planet = 0
    for element in range(len(df.columns)):
        num = (element - 1)
        if num % 6 == 0:
            with open(filename5, 'a') as file:
                writer = csv.writer(file)
                data_point = [df.iat[line_number, element]]
                writer.writerow(data_point)
            planet += 1
if parameter == 'e':
    df = pd.read_csv(filename2)
    planet = 0
    for element in range(len(df.columns)):
        num = (element - 2)
        if num % 6 == 0:
            with open(filename5, 'a') as file:
                writer = csv.writer(file)
                data_point = [df.iat[line_number, element]]
                writer.writerow(data_point)
            planet += 1
if parameter == 'inc':
    df = pd.read_csv(filename2)
    planet = 0
    for element in range(len(df.columns)):
        num = (element - 3)
        if num % 6 == 0:
            with open(filename5, 'a') as file:
                writer = csv.writer(file)
                data_point = [df.iat[line_number, element]]
                writer.writerow(data_point)
            planet += 1
