# Plotting
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')


sns.lmplot(data=tips, x='total_bill', y='tip', col='smoker', row='time');