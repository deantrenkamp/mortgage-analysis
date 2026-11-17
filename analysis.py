import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("MORTGAGE30US.csv")
df["observation_date"] = pd.to_datetime(df["observation_date"])
df["MORTGAGE30US"] = pd.to_numeric(df["MORTGAGE30US"], errors="coerce")

# Clean: count and remove missing values
print("Missing values:", df["MORTGAGE30US"].isna().sum())
df = df.dropna()

# Summary numbers
print(df["MORTGAGE30US"].describe())
df["year"] = df["observation_date"].dt.year
yearly_avg = df.groupby("year")["MORTGAGE30US"].mean().round(2)
print(yearly_avg)

peak = df.loc[df["MORTGAGE30US"].idxmax()]
print("Peak rate:", peak["MORTGAGE30US"], "on", peak["observation_date"].date())

# Chart
plt.figure(figsize=(10, 5))
plt.plot(df["observation_date"], df["MORTGAGE30US"])
plt.title("30-Year Fixed Mortgage Rate (1971 to Present)")
plt.xlabel("Year")
plt.ylabel("Rate (%)")
plt.savefig("mortgage_rates.png")
plt.show()