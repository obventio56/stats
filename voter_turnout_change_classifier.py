import csv
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

def calc_cat(value, mean, std):
    bottom = norm.ppf(0.095, loc=mean, scale=std)
    top = norm.ppf(0.905, loc=mean, scale=std)
    bottom_2 = norm.ppf(0.2, loc=mean, scale=std)
    top_2 = norm.ppf(0.8, loc=mean, scale=std)
    dist = (value-mean)
    
    if value < bottom_2 or value > top_2:
        if value < bottom or value > top:
            return 2 
        else:
            return 1 
    else:
        return 0
    
    

data_points = []

with open('clean_data.csv', 'r') as f:
    data = csv.reader(f, delimiter=",")
    for row in data:
        data_points.append(row)

change_data = np.array([float(point[1]) for point in data_points])
mean = np.mean(change_data)
std = np.std(change_data)

plt.hist(change_data)
plt.xlabel("Change in Voter Turnout")
plt.ylabel("Frequency")
plt.savefig("distriubtion_of_change_in_turnout.png")

print(mean)
print(std)

change = [[],[],[]]
no_change = [[],[],[]]

for point in data_points:
    if point[2] == "t":
        change[calc_cat(float(point[1]), mean, std)].append(point[0])    
    else:
        no_change[calc_cat(float(point[1]), mean, std)].append(point[0])
        
print(change)
print(no_change)

print(len(change[0]))
print(len(change[1]))
print(len(change[2]))
print(len(no_change[0]))
print(len(no_change[1]))
print(len(no_change[2]))
