import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data.csv')

df = df.sort_values(df.columns[1], ascending = True)
X = df['Material']
Y = df['Conversion']

fig = plt.figure()
plt.plot(X, Y, 'b--')
ax = fig.add_subplot(111)
plt.xlabel('Material')
plt.ylabel('Conversion Performance')
for xy in zip(X, Y):                                       # <--
    ax.annotate('(%s, %s%%)' % xy, xy=xy, textcoords='data')

plt.grid()
plt.show()

