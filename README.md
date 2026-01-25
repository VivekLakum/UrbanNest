# UrbanNest
## 📌 Overview

When individuals relocate to a new city, selecting a suitable residential neighborhood becomes challenging due to the need to evaluate multiple urban factors simultaneously.

Information such as rental affordability and environmental quality is typically scattered across different platforms, forcing users to manually compare data and often leading to inefficient or biased decision-making.

UrbanNest addresses this problem by providing a data-driven neighborhood livability analysis system that integrates key urban indicators into a unified scoring framework, enabling easy and meaningful comparison of residential localities.

## 🎯 Objective

The primary objective of UrbanNest is to:

Analyze neighborhood livability using reliable urban data

Compare residential localities in a structured and explainable manner

Support relocation decisions through quantitative insights rather than intuition

## 🧠 Core Idea

UrbanNest computes a Livability Score for each locality by combining:

Housing Affordability
(calculated separately for different BHK categories to ensure fair economic comparison)

Air Quality Index (AQI)
(normalized into a comparable score for environmental assessment)

The final livability score provides a clear, locality-level ranking of residential areas.

## 📊 Data Sources
1. Housing Dataset

Includes:

Locality

BHK type

Rental price

Property attributes

Affordability is computed independently for:

1 BHK

2 BHK

3 BHK

This avoids distortion caused by mixing different housing categories.

2. AQI Dataset

Locality-level AQI values used for academic modeling

AQI values are normalized into a 0–1 score

Enables fair integration with affordability metrics

Note: AQI values represent estimated locality-level indices for analytical purposes and are not direct CPCB station measurements.

## ⚙️ Methodology
Step 1: Affordability Scoring

Calculated separately for each BHK type

Prevents unfair comparison between different housing categories

Scores normalized between 0 and 1

Step 2: AQI Normalization

AQI values are mapped to a standardized environmental score:

AQI Range	Score
0–50	1.0
51–100	0.8
101–200	0.6
201–300	0.4
301–400	0.2
401–500	0.0
Step 3: Livability Score Calculation
Livability Score
=
0.6
×
Affordability Score
+
0.4
×
AQI Score
Livability Score=0.6×Affordability Score+0.4×AQI Score

This weighted model reflects the higher influence of housing affordability while still accounting for environmental quality.

## 📈 Output

UrbanNest generates:

Livability score for each locality

Ranked list of neighborhoods

Visual comparisons across areas

This enables users to quickly identify relatively more livable residential zones.

## 🧪 Technologies Used

Python

Pandas

NumPy

Scikit-learn

Matplotlib

Jupyter Notebook

## ✅ Key Highlights

BHK-wise affordability modeling

Explainable scoring logic

Normalized multi-factor comparison

Clean and interpretable results

Internship-ready analytical structure

🔮 Future Scope

UrbanNest can be extended to include:

Commute accessibility analysis

Amenity density scoring

Interactive web dashboard

Real-time data integration

These enhancements can further improve decision accuracy as additional reliable data becomes available.

## 📌 Conclusion

UrbanNest demonstrates how urban data can be structured and analyzed to support residential decision-making.
By focusing on clarity, fairness, and explainability, the system provides a strong foundation for scalable urban livability analysis
