# Analysis
import pandas as pd
import numpy as np

# Plotting
import matplotlib.pyplot as plt
import seaborn as sns

houses = {'area' : [40, 50, 60, 70, 80],
          'price': [120000, 150000, 200000,
                    250000, 300000]}
df = pd.DataFrame(houses)
sns.lmplot(x='area',y='price',data=df)
plt.xlabel('Area (metres sq.)')
plt.ylabel('Price (€)')
plt.show()