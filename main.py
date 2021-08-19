
import numpy as np
import matplotlib.pyplot as plt


x = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
y = [400, 800, 1000, 2500, 3000, 5000, 7000, 10000, 30000, 50000]
n_group:10
plt.xlabel('year')
plt.ylabel('visitors')
plt.plot(x, y)
plt.show()

# data to plot
n_groups = 11
means_2008 = (47607, 14269, 8771, 3719, 5988, 720, 1574, 4884, 1354, 11653, 15177)
means_2017 = (46358, 37068, 12356, 6231, 7187, 824, 2336, 9079, 2779, 12118, 26722)

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, means_2008, bar_width,
alpha=opacity,
color='r',
label='2008')

rects2 = plt.bar(index + bar_width, means_2017, bar_width,
alpha=opacity,
color='g',
label='2017')

plt.xlabel('Countries')
plt.ylabel('Visitors')
plt.title('International Visitors')
plt.xticks(index + bar_width, ('UK', 'Ger', 'Fr', 'Italy', 'NeLds', 'Greece', 'B&L', 'Swi', 'Austria', 'Scan', 'CIS&EE'))
plt.legend()

plt.tight_layout()
plt.show()