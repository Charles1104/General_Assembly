import pandas as pd
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import matplotlib.pyplot as plt
import thinkplot
import thinkstats2
from scipy import stats

# Read the data file
data = pd.read_csv('dataset.csv', encoding="ISO-8859-1")

data['status_binary'] = data.status.apply(lambda x: 1 if x == "successful" else 0)

# histogram of duration for successful and live projects
succ = data[data.status_binary == 1]
print(min(succ.duration), max(succ.duration), stats.mode(succ.duration))

hist1, bin_edges = np.histogram(succ.duration, bins=range(100))
plt.bar(bin_edges[:-1], hist1, width=1)
plt.xlim(min(bin_edges), max(bin_edges))
plt.show()