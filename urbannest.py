import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🏙️ Pune Livability Analysis")

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv("dataset/pune_rent.csv")

# -----------------------------
# USER INPUT
# -----------------------------
selected_bhk = st.selectbox(
    "Select BHK type",
    ["1bhk", "2bhk", "3bhk"]
)

bhk_map = {
    "1bhk": "avg_rent_1bhk",
    "2bhk": "avg_rent_2bhk",
    "3bhk": "avg_rent_3bhk"
}

rent_col = bhk_map[selected_bhk]


# -----------------------------
# AFFORDABILITY
# -----------------------------
min_rent = df[rent_col].min()
max_rent = df[rent_col].max()

df["affordability_score"] = (
    100 * (max_rent - df[rent_col]) /
    (max_rent - min_rent)
)

# -----------------------------
# NORMALIZE AQI
# -----------------------------
aqi_min = df["AQI_Score"].min()
aqi_max = df["AQI_Score"].max()

df["AQI_Normalized"] = (
    100 * (df["AQI_Score"] - aqi_min) /
    (aqi_max - aqi_min)
)

# -----------------------------
# LIVABILITY
# -----------------------------
df["Livability_Score"] = (
    0.6 * df["affordability_score"] +
    0.4 * df["AQI_Normalized"]
)

# -----------------------------
# RESULTS
# -----------------------------
top10 = df.sort_values("Livability_Score", ascending=False).head(10)

st.subheader("Top 10 Most Livable Areas")
st.dataframe(top10[["locality", "Livability_Score"]])

# -----------------------------
# PLOT
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
