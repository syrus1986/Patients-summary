import pandas as pd

# Load dataset
df = pd.read_csv("patients.csv")

# Convert dates
df["arrival_date"] = pd.to_datetime(df["arrival_date"], dayfirst=True, errors="coerce")
df["departure_date"] = pd.to_datetime(df["departure_date"], dayfirst=True, errors="coerce")

# Calculate length of stay
df["length_of_stay"] = (df["departure_date"] - df["arrival_date"]).dt.days

# Define analysis variables
summary_stats = df.describe()
avg_satisfaction = df.groupby("service")["satisfaction"].mean().sort_values(ascending=False)
age_distribution = df["age"].describe()
longest_stays = df.nlargest(10, "length_of_stay")[["name", "service", "length_of_stay"]]

# Export to Excel
with pd.ExcelWriter("patient_analysis.xlsx") as writer:
    df.to_excel(writer, sheet_name="Raw Data", index=False)
    summary_stats.to_excel(writer, sheet_name="Summary Stats")
    avg_satisfaction.to_excel(writer, sheet_name="Avg Satisfaction")
    age_distribution.to_excel(writer, sheet_name="Age Distribution")
    longest_stays.to_excel(writer, sheet_name="Longest Stays", index=False)

print("Report exported to patient_analysis.xlsx")
