import matplotlib.pyplot as plt
import seaborn as sns


class HappinessVisualizer:
    """
    Class to create plots for World Happiness Report data.
    """

    def __init__(self, data):
        self.data = data

    def plot_top_countries(self, n=10):
        """
        Bar plot of top n countries based on Weighted_Score averaged over all years.
        """
        df_avg = self.data.groupby("Country")["Weighted_Score"].mean().reset_index()
        df_top = df_avg.nlargest(n, "Weighted_Score")
        plt.figure(figsize=(10, 5))
        sns.barplot(x="Weighted_Score", y="Country", data=df_top)
        plt.title(f"Top {n} countries by Weighted Score (2015-2019)")
        plt.show()

    def plot_correlation(self, x=None, y=None, year=None):
        """
        Scatter plot showing correlation between two metrics.
        x, y: column names to plot (e.g., 'GDP per capita', 'Social support', 'Weighted_Score', etc.)
        If year is provided, plots only for that year.
        """
        # If user doesn't provide columns, use defaults
        if x is None or y is None:
            x = "GDP per capita"
            y = "Weighted_Score"

        # Filter by year if specified
        if year:
            df = self.data[self.data["Year"] == year]
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

    def plot_trend(self, country):
        """
        Line plot of Weighted_Score over years for a specific country.
        """
        df_country = self.data[self.data["Country"] == country]
        plt.figure(figsize=(8, 6))
        sns.lineplot(x="Year", y="Weighted_Score", data=df_country, marker="o")
        plt.title(f"Weighted Score trend over years for {country}")
        plt.show()
