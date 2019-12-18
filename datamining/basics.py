# basic plots

# scatterplots - visualizing relationship between two pai pieces of data
from matplotlib import pyplot as plt
friends = [ 70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label, 
        xy=(friend_count, minute_count),
        xytext=(5, -5),
        textcoords='offset points'
    )

plt.title("Daily minutes vs NUmber of friends")
plt.xlabel("# of friiends")
plt.ylabel("daily minutes spent on site")