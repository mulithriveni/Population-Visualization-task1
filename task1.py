import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Age Group": ["0-14", "15-24", "25-54", "55-64", "65+"],
    "Population (%)": [26.16, 17.79, 41.24, 7.00, 7.81]
}

df = pd.DataFrame(data)

print(df)

plt.bar(df["Age Group"], df["Population (%)"])
plt.title("India Population Distribution (2022)")
plt.xlabel("Age Group")
plt.ylabel("Population %")
plt.show()

plt.hist(df["Population (%)"])
plt.title("Histogram")
plt.show()