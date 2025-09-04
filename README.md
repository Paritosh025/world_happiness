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

- **Data Handling (HappinessHandler):**  
  - Load yearly datasets (2015–2019)  
  - Clean and merge datasets  
  - Compute Weighted Score  
  - Rank countries & fetch top N countries  
  - Check country-specific ranks and scores  

- **Visualization (HappinessVisualizer):**  
  - Plot top N happiest countries  
  - Explore correlations between factors (e.g., GDP vs Weighted Score)  
  - Show happiness trend of a specific country over time  

For full function explanations **with code**, see the [TUTORIAL.md](./TUTORIAL.md).  

---
