import pandas as pd
import matplotlib.pyplot as plt

# Load dataset (working link)
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/flights.csv")

print(df.head())

# Pivot for better visualization
pivot_df = df.pivot(index="month", columns="year", values="passengers")

# Plot heatmap-style (using matplotlib)
plt.imshow(pivot_df, aspect='auto')
plt.colorbar(label="Passengers")
plt.title("Flight Passengers Over Years")
plt.xlabel("Year")
plt.ylabel("Month")
plt.show()