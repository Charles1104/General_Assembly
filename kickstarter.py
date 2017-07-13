import pandas as pd
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import matplotlib.pyplot as plt
import thinkplot
import thinkstats2
import scipy


# Read the data file
data = pd.read_csv('dataset.csv', encoding="ISO-8859-1")

# Print the mean with all the values
print('Mean with all the values: ', data.pledged.mean())

# Replace the 0 values by 'nan'
na_vals = [0.0]
data.pledged.replace(na_vals, np.nan, inplace=True)

# Print the mean without the 0 values
print('Mean without the 0 values: ', data.pledged.mean())

# Create a histogram for the number of backers
# with thinkstats2 and Thinkplot
hist1 = thinkstats2.Hist(data.backers, label='backers')
thinkplot.Hist(hist1)
thinkplot.Show(xlabel='value', ylabel="frequency")

hist2, bin_edges = np.histogram(data.backers, bins=range(20000))
plt.bar(bin_edges[:-1], hist2, width=1)
plt.xlim(min(bin_edges), max(bin_edges))
plt.show()
# skewness of the distribution
print('skewness of backers', scipy.stats.skew(data.backers, axis=0, bias=True))

# check for normality in the distribution
print('normality of duration', scipy.stats.mstats.normaltest(data.duration, axis=0))