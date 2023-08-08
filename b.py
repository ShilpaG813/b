import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
t=pd.read_csv(r'C:\Users\shilp\Onedrive\Desktop\iris.csv')
sns.set(style='white',color_codes=False)
sns.boxplot(x='Species',y='SepalLengthCm',data=t)
plt.title('Box plot for iris')
plt.show()