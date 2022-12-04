import pandas as pd
import numpy as np 
import random 
import matplotlib.pyplot as plt

t = 15
data = pd.date_range(start='1/1/2022 10:00:00', end='1/1/2022 17:00:00', freq= str(t)+'min')
df = pd.DataFrame(
    {
        "Date" : data
    }
)
df.index = np.arange(1, len(df) + 1)
lst = []
for i in range(len(df)):
    ran = random.uniform(20, 30)
    ran2 = round(ran, 2)
    lst.append(ran2)
df = df.assign(Temperature = lst)
plt.plot(df["Date"], df["Temperature"])
plt.show()