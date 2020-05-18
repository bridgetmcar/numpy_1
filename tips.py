import csv
import numpy as np

with open("tips.csv", "r") as file:
  data = csv.reader(file,delimiter=",")
  headers = next(data)
  data_list = list(data)
  data_numpy = np.array(data_list)
  dtype = float

size = np.array(data_numpy[:,6], dtype=float)
tips = np.array(data_numpy[:,1], dtype=float)
bills = np.array(data_numpy[:,0], dtype=float)

tip_percentage = tips/bills*100

print(round(tip_percentage.mean(),2))
