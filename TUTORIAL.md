# Happiness Package Tutorial

This tutorial demonstrates how to use the `happiness` package for loading, processing, and visualizing World Happiness Report data.

---

## 1. Import the package

```python

from .happiness_handler import HappinessHandler
from .happiness_visualizer import HappinessVisualizer

from happiness import HappinessHandler, HappinessVisualizer
```

## 2. Load data
### Initialize the handler and load datasets:
I initialize the handler and load the World Happiness Report data. <br>
One can also load a single year or combine multiple years for analysis.
```python

def load_data(self, year):
    """
    Load dataset for a given year (2015–2019)
    """
    file_map = {
        2015: "2015.csv",
        2016: "2016.csv",
        2017: "2017.csv",
        2018: "2018.csv",
        2019: "2019.csv"
    }

    if year not in file_map:
        raise ValueError(f"Data for year {year} not available")

    path = os.path.join(self.data_dir, file_map[year])

    if not os.path.exists(path):
        raise FileNotFoundError(f"{path} does not exist")

    self.data = pd.read_csv(path)
    return self.data

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
## 3. Compute Weighted_Score

The dataset already includes a Score column, but it doesn’t always allow for custom analysis, since some factors are ignored or underrepresented. To get a more meaningful measure, we calculate a weighted happiness score.<br>

Each factor contributes differently to overall happiness:<br>

GDP per capita – major contributor `0.3`<br>
Social support – significant contributor `0.25`<br>
Healthy life expectancy – important factor `0.2`<br>
Freedom to make life choices – moderate influence `0.15`<br>
Perceptions of corruption – minor influence`0.05`<br>
Generosity – minor influence `0.05`<br>

By assigning different weights to these indicators, the weighted score captures a more balanced and interpretable measure of happiness for each country. This allows for self-analysis and comparison across countries in a way that reflects the relative importance of these factors.

```python

def compute_weighted_score(self):
    w = {
        'GDP per capita': 0.3,
        'Social support': 0.25,
        'Healthy life expectancy': 0.2,
        'Freedom to make life choices': 0.15,
        'Perceptions of corruption': 0.05, # Generally does not contribute much
        'Generosity': 0.05 # It does not contribute much
     }
self.data['Weighted_Score'] = (
            self.data['GDP per capita'] * w['GDP per capita'] +
            self.data['Social support'] * w['Social support'] +
            self.data['Healthy life expectancy'] * w['Healthy life expectancy'] +
            self.data['Freedom to make life choices'] * w['Freedom to make life choices'] +
            self.data['Perceptions of corruption'] * w['Perceptions of corruption'] +
            self.data['Generosity'] * w['Generosity']
)

hh.compute_weighted_score()

```

## 4. Get top countries

### This function identifies the top n happiest countries based on the weighted score:
1. First, it ensures that the weighted score is computed for all countries.
2. Then, it calculates the average weighted score for each country across all available years.
3. Finally, it ranks the countries and selects the top n with the highest average scores.

```python
def get_top_countries(self, n=10):
        
    self.compute_weighted_score()  # ensure column exists
    df_avg = self.data.groupby('Country')['Weighted_Score'].mean().reset_index()
    df_top = df_avg.nlargest(n, 'Weighted_Score')
    return df_top

top_countries = hh.get_top_countries(n=10)
print(top_countries)
```


## 5. Get rank of a country
### This function allows you to check how a specific country ranks based on the weighted score.
1. First, it ensures that the weighted score is computed for all countries.
2. Then, it calculates the average weighted score for each country and sorts them in descending order.
3. Finally, it finds the rank of the requested country, returns the total number of countries, and its average score.


```python
def get_country_rank(self, country):
       
     self.compute_weighted_score()  # ensure column exists
     df_avg = self.data.groupby('Country')['Weighted_Score'].mean().reset_index()
     df_avg = df_avg.drop_duplicates(subset='Country')
     df_avg = df_avg.sort_values(by='Weighted_Score', ascending=False).reset_index(drop=True)

     try:
        rank = df_avg.index[df_avg['Country'] == country][0] + 1
     except IndexError:
        raise ValueError(f"{country} not found in dataset")

     total_countries = df_avg.shape[0]
     avg_score = df_avg.loc[df_avg['Country'] == country, 'Weighted_Score'].values[0]
     return int(round(rank)), int(total_countries), avg_score


country_name = input("Enter the country name to check its rank: ").strip()

try:
    rank, total_countries, avg_score = hh.get_country_rank(country_name)
    print(f"{country_name} ranks {rank} out of {total_countries} countries with an average score of {avg_score:.2f}")
except ValueError as e:
    print(e)
```

## 6. Visualize data
### Initialize the visualizer with the data:

```python
hv = HappinessVisualizer(hh.data)
```

## 7. Bar plot of top countries
This function creates a bar plot of the top n countries based on the average weighted score, making it easy to compare their overall happiness visually.

```python
def plot_top_countries(self, n=10):

    df_avg = self.data.groupby('Country')['Weighted_Score'].mean().reset_index()
    df_top = df_avg.nlargest(n, 'Weighted_Score')
    plt.figure(figsize=(10, 5))
    sns.barplot(x='Weighted_Score', y='Country', data=df_top)
    plt.title(f"Top {n} countries by Weighted Score (2015-2019)")
    plt.show()

hv.plot_top_countries(n=10)
```

## 8. Scatter plot correlation
This function creates a scatter plot showing the relationship between two variables, such as GDP per capita and weighted score.<br>
One can also filter the plot for a specific year to see year-wise correlations.
```python
def plot_correlation(self, x=None, y=None, year=None):

    # If user doesn't provide columns, use defaults
    if x is None or y is None:
        x = 'GDP per capita'
        y = 'Weighted_Score'

    # Filter by year if specified
    if year:
        df = self.data[self.data['Year'] == year]
    else:
        df = self.data

    # Check if columns exist
    if x not in df.columns or y not in df.columns:
        raise ValueError(f"Columns {x} and/or {y} not found in dataset")

    # Plot
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=x, y=y, data=df)
    plt.title(f"{y} vs {x}" + (f" in {year}" if year else ""))
    plt.show()

hv.plot_correlation(x='GDP per capita', y='Weighted_Score', year=2015)
```

## 9. Trend of weighted score over years for a country
This function plots the weighted score of a country over multiple years, showing its performance relative to key indicators like GDP, social support, and health across time.
```python
def plot_trend(self, country):
    """
    Line plot of Weighted_Score over years for a specific country.
    """
    df_country = self.data[self.data['Country'] == country]
    plt.figure(figsize=(8, 6))
    sns.lineplot(x='Year', y='Weighted_Score', data=df_country, marker='o')
    plt.title(f"Weighted Score trend over years for {country}")
    plt.show()

hv.plot_trend(country='Finland')
```
