import pandas as pd
import numpy as np
############1############
arr1 = np.random.randint(0, 100, 60).reshape(10,6)
df1 = pd.DataFrame(arr1)
top = df1.head(5)
last = df1.tail(5)
############2############
arr2 = np.random.randint(0, 100, 24).reshape(6,4)
from datetime import date
today = date.today()
indexdf = []
for _ in range(0,6):
    indexdf.append(today)
columnsdf = ['A','B','C','D']
df2 = pd.DataFrame(
    arr2,
    columns = columnsdf,
    index = indexdf
    )
############3(4)############
arr3 = np.random.randint(0, 100, 60).reshape(10,6)
df3 = pd.DataFrame(arr3)
print(df3.columns)
print(df3.values)
############4(5)############
arr4 = np.random.randint(0, 100, 60).reshape(10,6)
df4 = pd.DataFrame(arr4)
df4.describe()
############5############
arr5 = np.random.randint(0, 100, 60).reshape(10,6)
df5 = pd.DataFrame(arr5)
df5t = df5.transpose()
############6############
arr6 = np.random.randint(0, 100, 60).reshape(10,6)
columnsdf = ['A','B','C','D','E','F']
df6 = pd.DataFrame(arr6, columns= columnsdf)
df6 = df6.sort_values(by=['A'], ascending=False)
df6 = df6.sort_values(by=['B'], ascending=False)
df6 = df6.sort_values(by=['C'], ascending=False)
df6 = df6.sort_values(by=['D'], ascending=True)
df6 = df6.sort_values(by=['E'], ascending=True)
df6 = df6.sort_values(by=['F'], ascending=True)
############7############
arr7 = np.random.randint(0, 10, 60).reshape(10,6)
df7 = pd.DataFrame(arr7)
drm7 = df7[df7>7]
############8############
arr8 = np.random.randint(0, 10, 60).reshape(10,6)
df8 = pd.DataFrame(arr8)
drm8 = df8[df8>3]
drm8 = drm8.fillna(0)
############9############
arr9 = np.random.randint(0, 10, 60).reshape(10,6)
df9 = pd.DataFrame(arr9)
media = df9.mean()
mediana = df9.median()
prom = df9.mean()
###########10###########
arr10 = np.random.randint(0, 10, 60).reshape(10,6)
df10 = pd.DataFrame(arr10)
arr10s = np.random.randint(0, 10, 60).reshape(10,6)
df10s = pd.DataFrame(arr10s)
df10 = df10.append(df10s)
###########11###########
import string
arr11 = np.random.choice(list(string.ascii_lowercase),  size=(10,6))
df11 = pd.DataFrame(arr11)
df11c = pd.DataFrame(df11[0] + df11[1])
df11c[1] = df11[2] + df11[3]
df11c[2] = df11[4] + df11[5]
###########12###########
arr12 = np.random.randint(0, 10, 60).reshape(10,6)
df12 = pd.DataFrame(arr12)
for column in df12.columns:
    print("Column number:"+str(column))
    r = df12[column].value_counts()
    print(r)
###########13###########
arr13 = np.random.randint(0, 10, 30).reshape(10,3)
columns13 = ['A','B','C']
df13 = pd.DataFrame(
    arr13,
    columns = columns13,
    )
results = []
for index, row in df13.iterrows(): 
    results.append((row['A']+row['B'])/row['C'])
df13['results'] = results
