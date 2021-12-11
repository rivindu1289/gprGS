import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from pandas.core.frame import DataFrame

filename = "procOut1.txt"


file = open(filename)

df1 = pd.read_csv(file, sep=' ')
# print(df1.keys())

df = DataFrame()

xs = []
ts = []
a = []

for r in list(df1.index):
    for c in list(df1.columns):
        xs.append(float(c))
        ts.append(-1*float(r))
        a.append(float(df1.at[r,c]))

df["x"] = xs
df["t"] = ts
df["a"] = a

# print(df["a"])

# print(df)

df = df[df["t"] > -150]
df = df[df["x"] < 30]
df = df[df["x"] > 5]
df = df[df["a"].abs() > 20]

df["y"] = 0

df_copy1 = df.copy()

for i in range(40):
    df_copy = df_copy1.copy()
    df_copy["y"] = i
    df = df.append(df_copy, ignore_index=True)

df["a"] += np.random.normal(0, 5, df.shape[0])

MAX_AMP = max(max(df["a"]),abs(min(df["a"])))
# print(MAX_AMP)

df["color"] = (df["a"] + MAX_AMP) * 100. / MAX_AMP / 2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Depth")
ax.scatter(df["x"], df["y"], df["t"], c=df["color"], cmap='RdBu', s=1)
plt.show()