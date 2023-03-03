import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\cinshalewolfe\Desktop\my_repo\Assets\diamonds.csv')
print(df.head())

plt.scatter(df['carat'],df['price'], color='darkblue', edgecolor='red')