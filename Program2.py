# Plotting
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
sns.scatterplot(data=tips, x='total_bill', y='tip');

