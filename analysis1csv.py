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
file_number = filename0.split("_")[-1]
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

# #num of rows (len(df)) without header
# #num of cols (len(df.columns))

# # if line_number == '-1':
# if parameter == 'm':
#     with open(filename1, 'r') as f:
#         mycsv = csv.reader(f)
#         for row in mycsv:
#             text = row[1]
# #         # with open(filename1, 'rb') as f:
# #         #     mycsv = csv.reader(f)
# #         #     mycsv = list(mycsv)
# #         #     text = mycsv[-1][2]
#             print(text)
# #             #
# #             # rows = list(csv.reader(f))
# #             # print(rows[-1][2])
# #             # #
# #             # lines = f.read().splitlines()
# #             # last_line= lines[-1]
# #             # print(last_line)
# #         f.close()

# else:
filename5 = "output.{0}.time{1}.csv".format(parameter,line_number*100)

filename666 = "output.dump.time{0}".format(line_number * 100)

with open(filename5, 'a') as file:
    if parameter == 'm':
        df = pd.read_csv(filename1)
        # planet = 0
        for element in range(len(df.columns)):
            num = (element - 1)
            if num % 8 == 0:
                writer = csv.writer(file)
                data_point = [df.iat[line_number, element]]
                if np.isnan(data_point):
                    continue
                else:
                    writer.writerow(data_point)
            # planet += 1
        del df

    if parameter == 'aei':
        # if line_number == '-1':
        with open(filename1, 'rb') as f:
            try:  # catch OSError in case of a one line file
                f.seek(-2, os.SEEK_END)
                while f.read(1) != b'\n':
                    f.seek(-2, os.SEEK_CUR)
            except OSError:
                f.seek(0)
            # print('file_number = ', file_number)
            cart_last_line = f.readline().decode().split(',')
            cart_last_line[-1]=cart_last_line[-1].split("\r")[0]
            # print(cart_last_line)
            cart_num_of_object = int(np.floor(len(cart_last_line) - 1) / 8) #start after the star in the 0 positions -1
            cart_num_of_planets = cart_num_of_object -1
            # print("num_of_planets: ", cart_num_of_planets)
            N = 0
            N = cart_num_of_planets
            # for planet_index in range(cart_num_of_planets):
                # print(cart_last_line[planet_index * 8 + 1])
                # we don't want the sun only the planets
                # if float(cart_last_line[(planet_index+1) * 8 + 1]) < 0.999:
                #     N = N + 1

            cart_planets = [[]] * N
            print(len(cart_planets))
            print(len(cart_last_line))
            for planet_index in range(cart_num_of_planets):
                # print(planet_index)
              #  if float(cart_last_line[(planet_index+1) * 8 + 1])  < 0.999:
                    print((planet_index+1) * 8 + 1)
                    print((planet_index+1) * 8 + 1 + 2)
                    cart_planets[planet_index]= ( cart_last_line[(planet_index+1) * 8 + 1:(planet_index+1) * 8 + 1 + 2])

            for pp in cart_planets:
                print(pp)


        with open(filename2, 'rb') as f:
            try:  # catch OSError in case of a one line file
                f.seek(-2, os.SEEK_END)
                while f.read(1) != b'\n':
                    f.seek(-2, os.SEEK_CUR)
            except OSError:
                f.seek(0)
            last_line = f.readline().decode().split(',')
            last_line[-1]=last_line[-1].split("\r")[0]
            time = last_line[0]
            num_of_planets= int(np.floor(len(last_line)-1)/6)
            print("num_of_planets: ",num_of_planets)
            N = 0
            for planet_index in range(num_of_planets):
                if float(last_line[planet_index * 6 + 1]) > 0:
                    N = N + 1
            planets=[[]] *N
            for planet_index in range(num_of_planets):
                # print(planet_index)
                if float(last_line[planet_index*6+1])>0:
                    planets[planet_index]=last_line[planet_index*6+1:planet_index*6+1+6]
                    planets[planet_index].append(cart_planets[planet_index][0])
                    planets[planet_index].append(cart_planets[planet_index][1])

                else:
                    dump = last_line[planet_index*6+1:planet_index*6+1+6]
                    dump.append(cart_planets[planet_index][0])
                    dump.append(cart_planets[planet_index][1])
                    dump.append(file_number)
                    dump.append(time)

                    with open(filename666, 'a') as file2:
                        writer = csv.writer(file2)
                        writer.writerow(dump)
                    # N=N+1
                    print('dump= ',dump)
            for planet in planets:
                print(planet)
            for planet in cart_planets:
                print(planet)
            # todo here add the m hash to the orbital element BEFORE DAMPING UNBOUND PARTICALS
            # sorting the planets array by the semi major axis
            sorted_planets= sorted(planets, key=lambda orbital_elements: float(orbital_elements[0])) #reverse=True
            # print(planets)

            print('N' , N)
            for planet in sorted_planets:
                print(planet[0])

            if N >0:
                new_last_line= [sorted_planets[0:N]]
                new_last_line= sum(new_last_line,[])

            # print(new_last_line)
            #flat_list = list(np.concatenate(new_last_line).flat)
                last_line = sum(new_last_line, [file_number, time])
            # print(last_line)

            filename6 = "output.{1}p.time{0}.V5.csv".format(line_number * 100,N)

            with open(filename6, 'a') as file2:
                writer = csv.writer(file2)
                writer.writerow(last_line)



            # for element in range(len(last_line)):
            #     data_row = [time]
            #     num = (element - 1)
            #     if num % 6 == 0:
            #         data_point1 = last_line[element]
            #         data_row.append(data_point1)
            #         data_point2 = last_line[element+1]
            #         data_row.append(data_point2)
            #         data_point3 = last_line[element+2]
            #         data_row.append(data_point3)
            #         periastron = float(data_point1)*(1-float(data_point2))
            #         data_row.append(periastron)
            #         planet = planet+ 1
            #         data_row.append(planet)
            #         writer = csv.writer(file)
            #         writer.writerow(data_row)


        # ChunkSize = 10000
        # for chunk in pd.read_csv(filename2, ChunkSize= ChunkSize,skiprows= line_number, keep_default_na= False):
        #     df = chunk
        #     # df = pd.read_csv(filename2)
        #     planet = 0
        #     for element in range(len(df.columns)):
        #         data_row = []
        #         num = (element - 1)
        #         if num % 6 == 0:
        #             data_point1 = df.iat[line_number, element]
        #             data_row.append(data_point1)
        #             if np.isnan(data_point):
        #                 continue
        #             else:
        #                 data_point2 = df.iat[line_number, element+1]
        #                 data_row.append(data_point2)
        #                 data_point3 = df.iat[line_number, element+2]
        #                 data_row.append(data_point3)
        #                 periastron = data_point1*(1-data_point2)
        #                 data_row.append(periastron)
        #                 planet = + 1
        #                 data_row.append(planet)
        #                 writer = csv.writer(file)
        #                 writer.writerow(data_row)
        #
        #     del df

    # if parameter == 'coll':
    #     df = pd.read_csv(filename3)
    #     del df
    # if parameter == 'eject':
    #     df = pd.read_csv(filename4)
    #     del df
