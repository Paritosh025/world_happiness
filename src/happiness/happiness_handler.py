import pandas as pd
import os


class HappinessHandler:
    """
    Class to load, clean, and handle World Happiness Report data.
    """

    def __init__(self, data_dir="../data"):
        self.data_dir = data_dir
        self.data = pd.DataFrame()

    def load_data(self, year):
        """
        Load dataset for a given year (2015–2019)
        """
        file_map = {
            2015: "2015.csv",
            2016: "2016.csv",
            2017: "2017.csv",
            2018: "2018.csv",
            2019: "2019.csv",
        }

        if year not in file_map:
            raise ValueError(f"Data for year {year} not available")

        path = os.path.join(self.data_dir, file_map[year])

        if not os.path.exists(path):
            raise FileNotFoundError(f"{path} does not exist")

        self.data = pd.read_csv(path)
        return self.data

    def compute_weighted_score(self):
        """
        Adds a Weighted_Score column to the data based on selected factors,
        Here exclude scores as they gave direct result so use other attributes
        """
        w = {
            "GDP per capita": 0.3,
            "Social support": 0.25,
            "Healthy life expectancy": 0.2,
            "Freedom to make life choices": 0.15,
            "Perceptions of corruption": 0.05,  # Generally does not contribute much
            "Generosity": 0.05,  # It does not contribute much
        }
        self.data["Weighted_Score"] = (
            self.data["GDP per capita"] * w["GDP per capita"]
            + self.data["Social support"] * w["Social support"]
            + self.data["Healthy life expectancy"] * w["Healthy life expectancy"]
            + self.data["Freedom to make life choices"]
            * w["Freedom to make life choices"]
            + self.data["Perceptions of corruption"] * w["Perceptions of corruption"]
            + self.data["Generosity"] * w["Generosity"]
        )

    def get_top_countries(self, n=10):
        """
        Return top n countries based on Weighted_Score averaged over all years.
        """
        self.compute_weighted_score()  # ensure column exists
        df_avg = self.data.groupby("Country")["Weighted_Score"].mean().reset_index()
        df_top = df_avg.nlargest(n, "Weighted_Score")
        return df_top

    def get_country_rank(self, country):
        """
        Returns rank of a specific country based on Weighted_Score averaged over all years.
        Assumes that compute_weighted_score() has already been called once.
        """
        # Group by country and take the mean Weighted_Score
        df_avg = self.data.groupby("Country")["Weighted_Score"].mean().reset_index()

        # Sort countries by score (highest first)
        df_avg = df_avg.sort_values(by="Weighted_Score", ascending=False).reset_index(drop=True)

        # Try to get the country's rank
        try:
            rank = df_avg.index[df_avg["Country"] == country][0] + 1
        except IndexError:
            raise ValueError(f"{country} not found in dataset")

        total_countries = df_avg.shape[0]
        avg_score = df_avg.loc[df_avg["Country"] == country, "Weighted_Score"].values[0]

        return int(rank), int(total_countries), avg_score

