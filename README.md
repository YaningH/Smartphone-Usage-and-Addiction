# Smartphone Usage and Addiction: An Exploratory Data Analysis
**Author:** Yaning Hu
**Course:** Python: Data, Science & Design 
**Date:** Spring 2025

---

## Overview

Smartphones have become one of the most widely used technologies in daily life, particularly among young adults. While they offer convenience and connectivity, concerns about overuse and addiction have grown significantly in recent years. This project uses exploratory data analysis to investigate what smartphone usage behaviors are most strongly associated with addiction levels among users aged 18 to 35. By examining patterns across screen time, social media use, age groups, and weekend behavior, this analysis aims to identify which habits most clearly separate mild users from those showing signs of severe addiction.

---

## Research Question

**What smartphone usage behaviors are most strongly associated with addiction level among users aged 18–35?**

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

### 1. Daily Screen Time Is the Strongest Indicator of Addiction

The most prominent finding in this dataset is the difference in daily screen time across addiction levels. Users classified as Mild average just **5.5 hours** of screen time per day, while Moderate users average **8.4 hours** and Severe users average **8.6 hours**. This is a gap of nearly 3 hours, which is meaningful in the context of daily life. The boxplot confirms this is not just an average effect, the entire distribution shifts upward from Mild to Moderate, with very little overlap between the two groups.

### 2. Social Media Hours Clearly Separate Mild from Addicted Users

Social media usage shows a clear stepwise increase across addiction levels. Mild users average **2.3 hours** per day on social media, while Moderate users average **3.6 hours** and Severe users average **3.8 hours**. This suggests that time spent on social media platforms is closely tied to addiction severity, and may be one of the predominant factors of overall screen time for more addicted users.

### 3. The Pattern Persists on Weekends

One possible explanation for high screen time is that work or school requires phone use during the week. However, the weekend screen time data does not support this. Mild users average **7.3 hours** on weekends, compared to **10.1 hours** for Moderate and **10.4 hours** for Severe users. The same pattern holds, which suggests that heavy phone use for more addicted users is a consistent behavioral pattern rather than a work-related necessity.

### 4. Older Users Are Slightly More Likely to Show Severe Addiction

When users are grouped by age, a mild but consistent trend emerges. Among users aged 18–21, approximately 34% fall into the Severe addiction category. This rises slightly to 36% for ages 22–25, 38% for ages 26–29, and stays at 37% for ages 30–35. Meanwhile, the percentage of Mild users decreases slightly as age increases, from 21% in the 18–21 group down to 19% in the 26–29 group. While this trend is not dramatic, it does suggest that addiction may deepen slightly with age rather than improving over time.

### 5. Daily and Weekend Screen Time Are Highly Correlated

The correlation heatmap reveals one very strong relationship: daily screen time and weekend screen time have a correlation of **0.96**, which is extremely high. This means that knowing a user's daily screen time almost perfectly predicts their weekend screen time. For all other feature pairs, correlations are close to zero, indicating that variables like age, sleep hours, gaming hours, and notifications per day do not strongly predict one another in this dataset.

### 6. Stress Level and Gender Do Not Differentiate Addiction

Two comparisons that initially seemed promising turned out to be flat. Stress level is almost perfectly evenly distributed across all addiction levels, roughly 33% Low, 33% Medium, and 34% High in every group. Similarly, gender showed no meaningful differences in screen time or social media hours between Male, Female, and Other users. These null findings are worth reporting because they tell us what does not predict addiction, which is as informative as what does.

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