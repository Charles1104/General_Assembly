import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import thinkplot
import thinkstats2
from scipy import stats
from collections import Counter
from operator import itemgetter

# Read the data file
data = pd.read_csv('dataset.csv', encoding="ISO-8859-1")

data['status_binary'] = data.status.apply(lambda x: 1 if x == "successful" else 0)

uni = np.unique(data.category)

dic = {}

for i in uni:
  data_filtered = data[data.category == i]
  success = Counter(data_filtered.status_binary)
  success['total'] = len(data_filtered)
  proportion = success[1] / success['total']
  dic[i] = proportion
print(sorted(dic.items(), key=itemgetter(1), reverse=True))
print(len(list(dic.keys())))
print(list(range(14)))

plt.bar(list(range(14)), dic.values(), color='g')
plt.xticks(list(range(14)), list(dic.keys()))
plt.show()