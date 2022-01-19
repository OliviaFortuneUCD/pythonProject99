# Analysis
import pandas as pd
import numpy as np

# Plotting
import matplotlib.pyplot as plt
import seaborn as sns

housesdub = {'area' : [40, 50, 60, 70, 80],
          'price': [120000, 150000, 200000,
                    250000, 300000]}
df = pd.DataFrame(housesdub)
housescork = {'area' : [40, 50, 60, 70, 80],
          'price': [120000, 150000, 200000,
                    250000, 200000]}
dfdub = pd.DataFrame(housesdub)
dfcork = pd.DataFrame(housescork)
corrdub = dfdub.corr()
corrcork = dfcork.corr()
print(corrdub)
print(corrcork)
