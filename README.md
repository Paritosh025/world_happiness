# 🌍 World Happiness Analysis (2015–2019)

## 📌 Problem Statement
The goal of this project is to **analyze global happiness trends** based on multiple social and economic parameters.  
Instead of relying on the direct "Happiness Score" column, a **Weighted Score** is computed by combining important factors with assigned weights:  

- GDP per capita (0.30)  
- Social support (0.25)  
- Healthy life expectancy (0.20)  
- Freedom to make life choices (0.15)  
- Perceptions of corruption (0.05)  
- Generosity (0.05)  

This approach gives a more balanced and fair estimate of happiness across countries and years.

---

## 📊 Dataset
The dataset comes from the official **[Kaggle World Happiness Report](https://www.kaggle.com/datasets/unsdsn/world-happiness)**.  

- Covers **5 years**: 2015 to 2019.  
- Data is provided as separate CSV files (`2015.csv`, `2016.csv`, …, `2019.csv`).  
- Columns across years were inconsistent → unnecessary ones were removed, and consistent features were kept.  
- Finally, all years were merged into **one unified dataset** for analysis.

---

## ⚙️ Project Structure
The project is organized as follows:

```{raw}
world_happiness/
├── data/                   # Raw datasets (2015.csv – 2019.csv)
├── notebooks/              # Jupyter / Colab notebooks
│   └── analysis.ipynb      # Main analysis notebook
├── src/
│   └── happiness/          # Core Python package
│       ├── __init__.py
│       ├── happiness_handler.py
│       └── happiness_visualizer.py
├── world_happiness.zip     # Zipped folder (src + data) for Colab use
├── requirements.txt        # Dependencies
├── pyproject.toml          # Project build / packaging config
├── LICENSE.txt
├── README.md               
└── TUTORIAL.md             # Detailed guide with code (function-by-function)
```

## 🔧 Features & Functionality
The project provides:  

- **Data Handling (HappinessHandler): (Data loading & Metrics) **
  - Load yearly datasets (2015–2019)  
  - Clean and merge datasets  
  - Compute Weighted Score  
  - Rank countries & fetch top N countries  
  - Check country-specific ranks and scores  

- **Visualization (HappinessVisualizer): (Plots)**  
  - Plot top N happiest countries  
  - Explore correlations between factors (e.g., GDP vs Weighted Score)  
  - Show happiness trend of a specific country over time  

For full function explanations **with code**, see the [TUTORIAL.md](./TUTORIAL.md).  

---

## 🚀 How to Run the Project  

You can run the project in two ways:  

### ✅ Option A — Google Colab (recommended for a quick start)  
- Open the notebook: **`notebooks/analysis.ipynb`** (or click the Colab badge at the top of this README).  
- The notebook guides you through:  
  - Uploading & unzipping **`world_happiness.zip`** (contains `src/happiness` and `data`).  
  - Running the analysis end-to-end.  
  - Generating rankings, trends, and visualizations.  

### 💻 Option B — Local Machine (VS Code / PyCharm)  
1. Clone or download this repo:  
   ```bash
   git clone https://github.com/Paritosh025/world_happiness.git
   cd world_happiness
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Open the notebook notebooks/analysis.ipynb in Jupyter, VS Code, or PyCharm.
4. Ensure that:
   - data/ contains yearly CSVs (2015–2019).
   - src/happiness/ is available (contains the package files).
5. Follow the same workflow as in Colab to reproduce the analysis.

---

## 📸 Screenshots  

(Add your own screenshots here for a more visual README. Place images in the `images/` folder and reference them below.)  

### Top 20 countries by chart / Colab setup  
![Colab setup](images/top_20_countries.png)  

### Weighted_Score vs GDP per Capita 
![Top 10 countries by Weighted Score](images/weighted_score_vs_gdp_per_capita.png)  

### Germany trend over time
![Trend for <Country> 2015–2019](images/weighted_score_trend.png) 

---

### Project overview / Colab setup
<img src="images/top_20_countries.png" alt="Colab setup" width="500">

### Top countries chart
<img src="images/weighted_score_vs_gdp_per_capita.png" alt="Top 10 countries" width="500">

### Country trend over time
<img src="images/weighted_score_trend.png" alt="Country trend" width="500">

---

## 📊 Interpreting Results  

- A **higher Weighted Score** indicates stronger performance across the chosen drivers, not just a single metric.  
- **Year-to-year changes** can reflect policy shifts, economic shocks, or measurement differences — use the trend plots to reason about stability vs. volatility.  
- **Correlation views** help visually check whether increases in a driver (e.g., GDP per capita) track with gains in the composite score.  

---

## ⚠️ Assumptions & Limitations  

- **Heuristic weights**: The weights reflect relative influence; they’re transparent and adjustable but not learned from a model.  
- **Schema drift**: Year-to-year changes in column names are normalized, but subtle definition changes may remain.  
- **Data coverage**: Analysis is limited to countries/years present in the Kaggle files.  

---

## 📑 Credits & License  

- **Data**: World Happiness Report (Kaggle).  
- **License**: See `LICENSE.txt` for details.  
- **Docs & How-to**: See `TUTORIAL.md`.

---

