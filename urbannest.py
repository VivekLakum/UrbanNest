import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("/content/Pune_Rent_Cleaned.csv")
import pandas as pd

# Load dataset

    bhk_map = {
        "1bhk": "avg_rent_1bhk",
        "2bhk": "avg_rent_2bhk",
        "3bhk": "avg_rent_3bhk"
    }
    st.write(df["bhk"].value_counts())


    rent_col = bhk_map[bhk_type]

    min_rent = df[rent_col].min()
    max_rent = df[rent_col].max()

    df_result = df.copy()

    df_result["affordability_score"] = (
        100 * (max_rent - df_result[rent_col]) /
        (max_rent - min_rent)
    ).round(2)

    return df_result.sort_values("affordability_score", ascending=False)


# -----------------------------
# Example usage
# -----------------------------
selected_bhk = input("Enter number of rooms")   # change to 1bhk / 2bhk / 3bhk

result = calculate_affordability(selected_bhk)

print(result[["locality", f"avg_rent_{selected_bhk}", "affordability_score"]].head(10))

import pandas as pd

aqi_df = pd.read_csv("/content/AQI_updated_with_score.csv")
aqi_df.head()
def clean(text):
    return text.strip().lower()

aqi_df["Locality_clean"] = aqi_df["Locality"].apply(clean)
df["Locality_clean"] = df["locality"].apply(clean)
merged_df = df.merge(
    aqi_df[["Locality_clean", "AQI_Score"]],
    on="Locality_clean",
    how="left"
)
merged_df[["locality", "AQI_Score"]].head(10)
merged_df["AQI_Score"].describe()
if 'Locality_clean' not in result.columns:
    result['Locality_clean'] = result['locality'].apply(clean)

merged_df = merged_df.merge(
    result[['Locality_clean', 'affordability_score']],
    on='Locality_clean',
    how='left'
)

merged_df["Livability_Score"] = (
    0.6 * merged_df["affordability_score"] +
    0.4 * merged_df["AQI_Score"]
)
livability_ranking = (
    merged_df.groupby("locality")["Livability_Score"]
    .mean()
    .sort_values(ascending=False)
)

livability_ranking.head(10)
import matplotlib.pyplot as plt

livability_ranking.head(10).plot(kind="bar")
plt.title("Top 10 Most Livable Areas in Pune")
plt.ylabel("Livability Score")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
final_df = merged_df[[
    "locality",
    "bhk",
    "affordability_score",
    "AQI_Score",
    "Livability_Score"
]]

final_df.to_csv("dataset/final_livability.csv", index=False)

