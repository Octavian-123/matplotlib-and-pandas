import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("marineLife.csv")

filtered = df[df["habitat"].str.contains ("ocean", case = False)]

print(filtered[["species", "common_name", "habitat"]])
