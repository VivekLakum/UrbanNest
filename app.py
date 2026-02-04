import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="UrbanNest", layout="wide")

st.title("🏙️ UrbanNest – Pune Livability Analyzer")

# -----------------------------
# LOAD DATA
# -----------------------------
@st.cache_data
def load_data():
    return pd.read_csv("dataset/pune_rent.csv")

df = load_data()

# -----------------------------
# USER INPUT
# -----------------------------
selected_bhk = st.selectbox(
    "Select BHK Type",
    ["1bhk", "2bhk", "3bhk"]
)

bhk_map = {
    "1bhk": "avg_rent_1bhk",
    "2bhk": "avg_rent_2bhk",
    "3bhk": "avg_rent_3bhk"
}

rent_col = bhk_map[selected_bhk]
df["Selected_BHK_Rent"] = df[rent_col]

# -----------------------------
# AFFORDABILITY SCORE
# -----------------------------
min_rent = df[rent_col].min()
max_rent = df[rent_col].max()

df["affordability_score"] = (
    100 * (max_rent - df[rent_col]) /
    (max_rent - min_rent)
)

# -----------------------------
# AQI NORMALIZATION
# -----------------------------
aqi_min = df["AQI_Score"].min()
aqi_max = df["AQI_Score"].max()

df["AQI_Normalized"] = (
    100 * (df["AQI_Score"] - aqi_min) /
    (aqi_max - aqi_min)
)

# -----------------------------
# LIVABILITY SCORE
# -----------------------------
rent_weight = st.slider("Rent Importance", 0.0, 1.0, 0.6)
aqi_weight = 1 - rent_weight

df["Livability_Score"] = (
    rent_weight * df["affordability_score"]
    + aqi_weight * df["AQI_Normalized"]
)


# -----------------------------
# TOP AREAS
# -----------------------------
top10 = df.sort_values("Livability_Score", ascending=False).head(10)

st.subheader("🏆 Top 10 Most Livable Areas")

st.dataframe(
    top10[["locality", "Selected_BHK_Rent", "Livability_Score"]],
    use_container_width=True
)
st.info(
    f"""
    Rankings are calculated using:
    - {rent_weight*100:.0f}% affordability
    - {aqi_weight*100:.0f}% air quality

    Lower rent + better AQI = higher livability.
    """
)


# -----------------------------
# BAR CHART
# -----------------------------
fig, ax = plt.subplots()
top10.plot(
    x="locality",
    y="Livability_Score",
    kind="bar",
    ax=ax,
    legend=False
)

plt.xticks(rotation=45)
st.pyplot(fig)
