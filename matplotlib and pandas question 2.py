import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("marineLife.csv")

species_count = df["species"].value_counts()

species_count.plot(kind="bar")

plt.title("Number of Each Species")
plt.xlabel("Species")
plt.ylabel("Count")

plt.show()
