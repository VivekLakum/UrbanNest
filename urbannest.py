import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# CONFIG
# -----------------------------
RENT_WEIGHT = 0.6
AQI_WEIGHT = 0.4

# -----------------------------
# LOAD DATA
# -----------------------------
rent_df = pd.read_csv("dataset/Pune_Rent_Cleaned.csv")
aqi_df = pd.read_csv("dataset/AQI_updated_with_score.csv")

# -----------------------------
# CLEAN LOCALITY NAMES
# -----------------------------
def clean(text):
    return text.strip().lower()

rent_df["Locality_clean"] = rent_df["locality"].apply(clean)
aqi_df["Locality_clean"] = aqi_df["Locality"].apply(clean)

# -----------------------------
# AFFORDABILITY FUNCTION
# -----------------------------
def calculate_affordability(df, bhk_type):
    bhk_map = {
        "1bhk": "avg_rent_1bhk",
        "2bhk": "avg_rent_2bhk",
        "3bhk": "avg_rent_3bhk"
    }

    if bhk_type not in bhk_map:
        raise ValueError("Choose only: 1bhk, 2bhk, 3bhk")

    rent_col = bhk_map[bhk_type]

    min_rent = df[rent_col].min()
    max_rent = df[rent_col].max()

    df = df.copy()

    df["affordability_score"] = (
        100 * (max_rent - df[rent_col]) /
        (max_rent - min_rent)
    ).round(2)

    return df


# -----------------------------
# SELECT BHK TYPE
# -----------------------------
selected_bhk = "2bhk"   # change here

rent_df = calculate_affordability(rent_df, selected_bhk)

# -----------------------------
# MERGE AQI DATA
# -----------------------------
merged_df = rent_df.merge(
    aqi_df[["Locality_clean", "AQI_Score"]],
    on="Locality_clean",
    how="left"
)

# -----------------------------
# LIVABILITY SCORE
# -----------------------------
merged_df["Livability_Score"] = (
    RENT_WEIGHT * merged_df["affordability_score"] +
    AQI_WEIGHT * merged_df["AQI_Score"]
).round(2)

# -----------------------------
# AREA RANKING
# -----------------------------
livability_ranking = (
    merged_df.groupby("locality")["Livability_Score"]
    .mean()
    .sort_values(ascending=False)
)

print("\nTop 10 Most Livable Areas in Pune:\n")
print(livability_ranking.head(10))

# -----------------------------
# VISUALIZATION
# -----------------------------
livability_ranking.head(10).plot(kind="bar")
plt.title("Top 10 Most Livable Areas in Pune")
plt.ylabel("Livability Score")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------------
# FINAL DATASET
# -----------------------------
final_df = merged_df[
    ["locality", "bhk", "affordability_score", "AQI_Score", "Livability_Score"]
]

final_df.to_csv("dataset/final_livability.csv", index=False)

print("\nfinal_livability.csv saved successfully.")
