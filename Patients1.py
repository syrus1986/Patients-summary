import pandas as pd
df=pd.read_csv("D:\Patients\patients.csv")
print(df)

print(df.head)
print(df.tail)
print(df.info)
print(df.describe)
print(df.index)
print(df.index.array)
print(df.isnull)



# # Convert arrival and departure dates to datetime
df["arrival_date"] = pd.to_datetime(df["arrival_date"], dayfirst=True, errors="coerce")
df["departure_date"] = pd.to_datetime(df["departure_date"], dayfirst=True, errors="coerce")

# # Calculate length of stay
df["length_of_stay"] = (df["departure_date"] - df["arrival_date"]).dt.days


# # Average satisfaction per service
avg_satisfaction = df.groupby("service")["satisfaction"].mean().sort_values(ascending=False)
print("\nAverage satisfaction per service:\n", avg_satisfaction)

# # Age distribution
print("\nAge distribution:\n", df["age"].describe())

# Top 10 longest stays
print("\nTop 10 longest stays:\n", df.nlargest(10, "length_of_stay")[["name", "service", "length_of_stay"]])

# # --- Visualizations ---
import matplotlib.pyplot as plt
# Satisfaction by service
plt.figure(figsize=(8,5))
avg_satisfaction.plot(kind="bar", color="skyblue")
plt.title("Average Satisfaction by Service")
plt.ylabel("Satisfaction Score")
plt.show()

# # Age histogram
plt.figure(figsize=(8,5))
df["age"].hist(bins=20, color="lightgreen", edgecolor="black")
plt.title("Age Distribution of Patients")
plt.xlabel("Age")
plt.ylabel("Number of Patients")
plt.show()

# # Length of stay histogram
plt.figure(figsize=(8,5))
df["length_of_stay"].hist(bins=15, color="salmon", edgecolor="black")
plt.title("Length of Stay Distribution")
plt.xlabel("Days")
plt.ylabel("Number of Patients")
plt.show()

# # --- Correlations ---
correlation_age_satisfaction = df["age"].corr(df["satisfaction"])
print("\nCorrelation between age and satisfaction:", correlation_age_satisfaction)

correlation_stay_satisfaction = df["length_of_stay"].corr(df["satisfaction"])
print("Correlation between length of stay and satisfaction:", correlation_stay_satisfaction)


