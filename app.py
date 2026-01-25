import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/content/final_livability.csv")

st.set_page_config(page_title="UrbanNest", layout="centered")

st.title("🏙️ UrbanNest – Neighborhood Livability Explorer")

bhk = st.selectbox("Select BHK Type", sorted(df["bhk"].unique()))

filtered = df[df["bhk"] == bhk]

st.subheader("Top 10 Livable Localities")

top10 = filtered.sort_values("Livability_Score", ascending=False).head(10)

st.dataframe(top10[["locality", "Livability_Score"]])

plt.figure(figsize=(8,4))
plt.bar(top10["locality"], top10["Livability_Score"])
plt.xticks(rotation=45)
plt.ylabel("Livability Score")
plt.tight_layout()
st.pyplot(plt)

st.markdown("""
### Livability Formula  
Livability = 0.6 × Affordability + 0.4 × AQI
""")
