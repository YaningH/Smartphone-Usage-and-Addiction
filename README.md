# Smartphone Usage and Addiction: An Exploratory Data Analysis
**Author:** Yaning Hu
**Course:** Python: Data, Science & Design 
**Date:** Spring 2025

---

## Overview

Smartphones are one of the most widely used technologies in our daily lives. There are ongoing conversations, particularly among young adults, about phone usage addiction, overuse, and increasing anxiety. This project intends to use exploratory data analysis to investigate which types of phone usage behaviors are most strongly tied to addiction levels and stress among users aged 18 to 35. By analyzing patterns across screen time, social media use, age groups, and weekend behavior. This analysis aims to identify which habits clearly distinguish mild users from those showing signs of severe addiction.

---

## Research Question

**What smartphone usage behaviors are most strongly associated with addiction level among users aged 18-35?**

Secondary questions explored:
- Does daily screen time clearly differ across addiction levels?
- Is social media usage a strong predictor of addiction severity?
- Does the pattern hold on weekends, or is it limited to weekdays?
- Do older users show higher rates of severe addiction than younger users?
- How do numeric usage features correlate with each other overall?

---

## Dataset Description

The dataset used in this analysis is the **Smartphone Usage and Addiction Analysis** dataset, sourced from Kaggle. It contains 7,500 rows and 16 columns, covering a range of smartphone usage behaviors and their associated outcomes for users aged 18 to 35.

### Features

The dataset contains a mix of numeric and categorical features:

**Numeric Features:**
| Feature | Description |
|---|---|
| `age` | Age of the user (18–35) |
| `daily_screen_time_hours` | Average daily screen time in hours |
| `social_media_hours` | Hours spent on social media per day |
| `gaming_hours` | Hours spent gaming per day |
| `work_study_hours` | Hours spent on work or study per day |
| `sleep_hours` | Average sleep hours per night |
| `notifications_per_day` | Number of phone notifications received per day |
| `app_opens_per_day` | Number of times apps are opened per day |
| `weekend_screen_time` | Average screen time on weekends in hours |

**Categorical Features:**
| Feature | Description |
|---|---|
| `gender` | Male, Female, or Other |
| `stress_level` | Self-reported stress: Low, Medium, or High |
| `addiction_level` | Classified as Mild, Moderate, or Severe |
| `academic_work_impact` | Whether phone use impacts academic or work life (Yes/No) |
| `addicted_label` | Binary label: 1 = addicted, 0 = not addicted |

### Data Cleaning

Of the 7,500 rows, 819 were missing a value for `addiction_level`. These rows were dropped before analysis, leaving 6,681 complete records. No other columns contained missing values. Age groups were created using `pd.cut()` to organize users into four ranges: 18–21, 22–25, 26–29, and 30–35.

---

## Key Findings

### 1. Social media accounts for nearly half of total screen time across all addiction levels

On average, social media usage accounts for approximately 45% of users' total daily screen time across all three addiction levels, making it the single largest category of phone use in this dataset. This consistent share across all addiction levels suggests that social media is not just a minor habit but the main way of how people spend time on their phones and likely one of the biggest contributors to addiction severity.

### 2. Weekend usage is higher across all groups, but the gap stays the same

On average, users spend about two more hours on their phones on weekends compared to weekdays, regardless of addiction level. One possible explanation for the lower weekday usage is that school or work naturally limits phone time during the week, structured schedules leave less opportunity for extended screen time. However, even accounting for this, heavily addicted users do not disproportionately binge on weekends. Their higher usage is consistent throughout the week, suggesting that addiction reflects a stable behavioral pattern rather than simply taking advantage of free time when it is available.

### 3. Age is not a meaningful predictor of addiction

The age range in this dataset spans 18 to 35, covering a wide variety of life stages, college students, early career working adults, and people who may be starting families. Despite these very different lifestyles and daily responsibilities, all four age groups show a nearly identical distribution: most users fall into Moderate, fewest into Mild, with Severe in between. The fact that this pattern holds regardless of whether someone is a 19 year old college student or a 33 year old with a full time job and a family suggests that age and life stage alone do not determine addiction severity. 

### 4. Only social media and screen time separate addiction groups, sleep and gaming do not

The pairplot provides a broader view of how all numeric features relate to each other across addiction levels. The diagonal distribution curves for sleep hours and gaming hours show almost complete overlap between Mild, Moderate, and Severe users, meaning that how much someone sleeps or games doesn't affect the smartphone addiction level as much. A Severe user is just as likely to get 7 hours of sleep or spend 2 hours gaming on smartphones as a Mild user. The scatter plots between most variable pairs also show no clustering by color, confirming that the majority of features do not predict each other. The exception is clear in the social media and daily screen time distributions, where the green cluster visibly separates from the orange and red. These are the only two variables where addiction groups show clear distinctions, which further proves that usage behavior on social platforms is where addiction most clearly manifests.

### 5. Stress level and gender do not differentiate addiction

Stress level is almost evenly split across all addiction groups. roughly one third Low, one third Medium, one third High in every group. Gender shows similarly flat patterns. These are important null findings. They tell us that addiction in this dataset is driven by usage behavior, not by who someone is or how stressed they feel.


---

## Visualizations

| Figure | Description |
|---|---|
| `fig1_screentime_addiction.png` | Average daily screen time by addiction level |
| `fig2_socialmedia_addiction.png` | Average social media hours by addiction level |
| `fig3_weekend_addiction.png` | Average weekend screen time by addiction level |
| `fig4_age_addiction.png` | Addiction level breakdown by age group (%) |
| `fig5_boxplot_screentime.png` | Distribution of screen time across addiction levels |
| `fig6_heatmap.png` | Correlation heatmap of all numeric features |
| `fig7_pairplot.png` | Pairplot of usage features colored by addiction level |

---

## Conclusions

This analysis found that smartphone addiction level is most clearly associated with **how much time users spend on their phones**, particularly daily screen time and social media hours. The gap between Mild and Moderate/Severe users is substantial, nearly 3 hours of screen time per day and this pattern holds consistently on weekends, suggesting it reflects a genuine behavioral difference rather than a work or school effect.

Age shows a modest trend, with older users being slightly more likely to fall into the Severe category. However, stress level and gender showed no meaningful differences, which is a useful finding in itself, it suggests that addiction in this dataset is more strongly tied to actual usage behavior than to demographic or psychological factors.

The correlation analysis confirmed that daily and weekend screen time are almost perfectly correlated (r = 0.96), reinforcing the idea that usage patterns are consistent across the week for heavily addicted users.

### Limitations

- The dataset appears to be synthetically generated, which may explain why many variables show near-zero correlations and perfectly even distributions across categories.
- Addiction level is a self-reported or algorithmically assigned label, the exact classification criteria are not documented.
- The dataset covers only users aged 18–35, so findings should not be generalized to children, teenagers, or older adults.
- This is an observational analysis, no causal claims can be made about whether screen time causes addiction or vice versa.

---

## How to Run

### Requirements
```bash
pip install pandas numpy matplotlib seaborn
```

### Steps
1. Download `Smartphone_Usage_And_Addiction_Analysis_7500_Rows.csv` from Kaggle
2. Place it in the same folder as `smartphone_eda.py`
3. Run the script:
```bash
python3 smartphone_eda.py
```
All 7 figures will be saved as `.png` files in the same folder.

### File Structure
```
project-folder/
├── smartphone_eda.py
├── Smartphone_Usage_And_Addiction_Analysis_7500_Rows.csv
├── README.md
└── figures/
    ├── fig1_screentime_addiction.png
    ├── fig2_socialmedia_addiction.png
    ├── fig3_weekend_addiction.png
    ├── fig4_age_addiction.png
    ├── fig5_boxplot_screentime.png
    ├── fig6_heatmap.png
    └── fig7_pairplot.png
```

---

## References

1. Kaggle. *Smartphone Usage and Addiction Analysis — 7500 Rows*. Retrieved from https://www.kaggle.com