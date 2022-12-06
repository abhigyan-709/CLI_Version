import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#create four DataFrames
df1 = pd.DataFrame({'x': np.linspace(0,10,10),
                    'y': np.random.rand(10)})
df2 = pd.DataFrame({'x': np.linspace(0,10,10),
                    'y': np.random.rand(10)})
df3 = pd.DataFrame({'x': np.linspace(0,10,10),
                    'y': np.random.rand(10)})
df4 = pd.DataFrame({'x': np.linspace(0,10,10),
                    'y': np.random.rand(10)})

# generating subplots
fig,axes = plt.subplots(nrows=2,ncols=2)

#plotting the dataframes
df1.plot(x='x', y='y', ax=axes[0][0])
df2.plot(x='x', y='y', ax=axes[0][1])
df3.plot(x='x', y='y', ax=axes[1][0])
df4.plot(x='x', y='y', ax=axes[1][1])

plt.show()