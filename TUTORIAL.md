# Happiness Package Tutorial

This tutorial demonstrates how to use the `happiness` package for loading, processing, and visualizing World Happiness Report data.

---

## 1. Import the package
```python
from happiness import HappinessHandler, HappinessVisualizer
```

## 2. Load data
## Initialize the handler and load datasets:
```
hh = HappinessHandler(data_dir="data")

# Load data for a single year
df_2015 = hh.load_data(2015)

# Or load multiple years
df_list = []
for year in range(2015, 2020):
    df_year = hh.load_data(year)
    df_year['Year'] = year
    df_list.append(df_year)

```
## 3. Compute Weighted Score
# These weighted scores are calculated based on a random formula, actually score column was already there restricting to perform self analysis and rest parameters were ignored so to tackle that I computed weighted_score given by this formula

hh.compute_weighted_score()

## 4. Get top countries

top_countries = hh.get_top_countries(n=10)
print(top_countries)

## 5. Get rank of a country

rank, total, score = hh.get_country_rank("Finland")
print(f"Rank: {rank}/{total}, Score: {score}")

## 6. Visualize data
## Initialize the visualizer with the data:

viz = HappinessVisualizer(hh.data)

# Bar plot of top countries
viz.plot_top_countries(n=10)

# Scatter plot correlation
viz.plot_correlation(x='GDP per capita', y='Weighted_Score', year=2015)

# Trend of weighted score over years for a country
viz.plot_trend(country='Finland')
