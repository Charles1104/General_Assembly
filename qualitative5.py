import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import thinkplot
import thinkstats2
from scipy import stats
from collections import Counter
from operator import itemgetter


def status(x):
  if x == "successful":
    return 1
  if x == "failed":
    return 0


def mapping_week(x):
  if x == 'Mon':
    return 1
  elif x == 'Tue':
    return 2
  elif x == 'Wed':
    return 3
  elif x == 'Thu':
    return 4
  elif x == 'Fri':
    return 5
  elif x == 'Sat':
    return 6
  elif x == 'Sun':
    return 7

# Read the data file
data = pd.read_csv('dataset.csv', encoding="ISO-8859-1")

data['status_binary'] = data.status.apply(status)

succ = data[data.status_binary == 1]
fail = data[data.status_binary == 0]

arr_success = []
arr_failure = []

for i in succ['funded date']:
  arr_success.append(i[:3])

for i in fail['funded date']:
  arr_failure.append(i[:3])

arr_success = list(map(mapping_week, arr_success))
arr_failure = list(map(mapping_week, arr_failure))

success = Counter(arr_success)
failure = Counter(arr_failure)

dic = {}

for i in range(1, 8):
  dic[i] = success[i] / (success[i] + failure[i])

plt.bar(list(range(1, 8)), dic.values(), color='g')
plt.xticks(list(range(1, 8)), ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
plt.show()