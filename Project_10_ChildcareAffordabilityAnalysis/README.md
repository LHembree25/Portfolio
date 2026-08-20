# Childcare Affordability and Maternal Labor Force Participation Analysis

This project analyzes childcare costs, household income, maternal labor‑force participation, and affordability burden using the National Database of Childcare Prices dataset. The workflow includes data ingestion, cleaning, transformation, ratio construction, correlation analysis, and multiple visualization builds. The notebook demonstrates technician‑level preprocessing, structured analysis, and multi‑layer visualization.

Cited from the attached document:  
“import pandas as pd… ndc_prices_df = pd.read_csv… nationaldatabaseofchildcareprices.csv”
“Compute the affordability ratios… ndc_prices_df['InfantCost_to_Income'] = ndc_prices_df['MCInfant'] / ndc_prices_df['MHI']”

## Tools Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

## Notebook Contents
- Data ingestion and preview of 227‑column childcare dataset
- Cleaning of monetary fields and household structure fields
- Filtering unstable counties using Under‑6 household totals
- Construction of affordability ratios (infant, toddler, preschool)
- Center‑based vs FCC cost comparisons
- Correlation matrix and maternal labor‑force participation analysis
- Identification of counties with highest affordability burden
- Identification of counties with lowest maternal labor‑force participation
- Multiple visualization builds:
  - Scatterplot of cost‑to‑income vs maternal participation
  - Horizontal bar charts for affordability burden
  - Participation distribution histograms
  - Binned regression plots
  - Violin plots
  - Band charts
  - Slope graphics
  - Tile grid infographic

## Key Results
- Infant cost‑to‑income ratios highlight counties with the highest affordability burden.
  - Example from the document: Whitman County at 0.010391
- Maternal labor‑force participation varies widely, with multiple counties showing 0.0 percent participation.
  - Example: “Menard County… 0.0”
- Correlation analysis shows maternal participation positively associated with household income and dual‑working households.
- Visualization builds confirm consistent patterns between childcare affordability and maternal workforce engagement.

## Why This Project Matters
This project demonstrates technician‑level data cleaning, ratio construction, correlation analysis, and multi‑visual storytelling. It supports workforce policy analysis, affordability research, and structured data presentation. The workflow is repeatable and suitable for operational dashboards, executive summaries, and exploratory modeling.
