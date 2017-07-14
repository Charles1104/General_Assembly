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


def status(x):
  if x == "successful":
    return 1
  if x == "failed":
    return 0


def mapping_month(x):
  if x == 'Jan':
    return 1
  elif x == 'Feb':
    return 2
  elif x == 'Mar':
    return 3
  elif x == 'Apr':
    return 4
  elif x == 'May':
    return 5
  elif x == 'Jun':
    return 6
  elif x == 'Jul':
    return 7
  elif x == 'Aug':
    return 8
  elif x == 'Sep':
    return 9
  elif x == 'Oct':
    return 10
  elif x == 'Nov':
    return 11
  elif x == 'Dec':
    return 12

data['status_binary'] = data.status.apply(status)

succ = data[data.status_binary == 1]
fail = data[data.status_binary == 0]

arr_success = []
arr_failure = []

for i in succ.funded_date:
  arr_success.append(i[8:11])

for i in fail.funded_date:
  arr_failure.append(i[8:11])

arr_success = list(map(mapping_month, arr_success))
arr_failure = list(map(mapping_month, arr_failure))

success = Counter(arr_success)
failure = Counter(arr_failure)

dic = {}

for i in range(1, 13):
  dic[i] = success[i] / (success[i] + failure[i])

plt.bar(list(range(1, 13)), dic.values(), color='g')
plt.xticks(list(range(1, 13)), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'])
plt.show()