
# with open("weather_data.csv") as data_file:
#   data = data_file.readlines()
#   print(data)

# import csv

# with open("weather_data.csv") as data_file:
#   csv_data = csv.reader(data_file)
#   temperatures = []
#   for row in csv_data:
#     if row[1] != "temp":
#       temperatures.append(int(row[1]))
#   print(temperatures)

import pandas as pd

data = pd.read_csv("weather_data.csv")
# print(data)

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

average_temp = sum(temp_list) / len(temp_list)
print(average_temp)

print(data["temp"].mean())

print(data["temp"].max())

# Get Data in Row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])