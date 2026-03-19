# Patients Summary Analysis

This repository contains a dataset of patient records and a Python script for analyzing and exporting insights into Excel.  
The goal is to provide descriptive statistics, satisfaction analysis, and visualizations for healthcare service evaluation.

---

## 📂 Dataset
The dataset (`patients.csv`) includes:
- **Patient ID**
- **Name**
- **Age**
- **Arrival & Departure Dates**
- **Service Type** (e.g., surgery, ICU, emergency, general medicine)
- **Satisfaction Score**

---

## 🧑‍💻 Analysis Script
The analysis script (`analysis.py`) performs the following tasks:

1. **Data Cleaning**
   - Converts arrival/departure dates to proper datetime format.
   - Calculates **length of stay** for each patient.

2. **Descriptive Statistics**
   - Summary statistics for age, satisfaction, and stay length.
   - Age distribution overview.

3. **Grouped Analysis**
   - Average satisfaction per service.
   - Satisfaction trends by length of stay.
   - Top 10 longest stays.

4. **Correlations**
   - Age vs. satisfaction.
   - Length of stay vs. satisfaction.

5. **Visualizations**
   - Bar chart: average satisfaction by service.
   - Histogram: age distribution.
   - Histogram: length of stay distribution.

---

## 📊 Excel Export
The script exports results into **`patient_analysis.xlsx`** with multiple sheets:

- `Raw Data` → Original patient dataset  
- `Summary Stats` → Descriptive statistics  
- `Avg Satisfaction` → Average satisfaction per service (with chart)  
- `Age Distribution` → Age statistics + embedded histogram  
- `Longest Stays` → Top 10 longest stays + embedded chart  
- `Stay vs Satisfaction` → Satisfaction grouped by stay length  
- `Correlations` → Age vs satisfaction, stay vs satisfaction  

Charts are embedded directly into the Excel file for easy visualization.

---

## ▶️ How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/syrus1986/Patients-summary.git
   cd Patients-summary
