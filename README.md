# 30-Year Mortgage Rate Analysis

A Python project that analyzes weekly 30-year fixed mortgage rates in the United States from 1971 to 2026.

## Data

- **Source:** Federal Reserve Economic Data (FRED), Federal Reserve Bank of St. Louis
- **Series:** MORTGAGE30US (30-Year Fixed Rate Mortgage Average in the United States, from Freddie Mac)
- **File:** `MORTGAGE30US.csv` (weekly observations)

## What the script does

1. Loads the CSV with pandas and converts dates and rates to the correct data types
2. Cleans the data by counting and removing missing values
3. Calculates summary statistics and the average rate for each year
4. Finds the peak rate and the date it occurred
5. Creates a line chart of rates over time and saves it as `mortgage_rates.png`

## Key findings

- The peak rate was **18.63%** on October 9, 1981
- The yearly average rose from **2.96% in 2021** to **6.81% in 2023**

## How to run

Install the required libraries:

```
python3 -m pip install pandas matplotlib
```

Run the script from the project folder:

```
python3 analysis.py
```

## Tools

Python, pandas, matplotlib
