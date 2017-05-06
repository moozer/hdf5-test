import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('SmaData_20160907.csv', delimiter='\t')
df.plot(x='Date', y='current W')
plt.show()
