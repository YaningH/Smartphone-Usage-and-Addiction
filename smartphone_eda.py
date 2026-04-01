import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Dataset: Smartphone Usage and Addiction Analysis
# Purpose: Explore patterns in smartphone usage and addiction levels among young adults

df = pd.read_csv('Smartphone_Usage_And_Addiction_Analysis_7500_Rows.csv')

print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())

# drop rows where addiction_level is missing
df = df.dropna(subset=['stress_level', 'addiction_level', 'gender'])

# create age groups for easier analysis
df['age_group'] = pd.cut(df['age'],
                          bins=[17, 21, 25, 29, 35],
                          labels=['18-21', '22-25', '26-29', '30-35'])

addiction_order = ['Mild', 'Moderate', 'Severe']

summary = {}
for level in addiction_order:
    subset = df[df['addiction_level'] == level]
    summary[level] = {
        'count':        len(subset),
        'screen_time':  subset['daily_screen_time_hours'].mean(),
        'social_media': subset['social_media_hours'].mean(),
        'weekend':      subset['weekend_screen_time'].mean()
    }
    print(f"{level}: n={summary[level]['count']} | "
          f"Screen={summary[level]['screen_time']:.1f}h | "
          f"Social={summary[level]['social_media']:.1f}h | "
          f"Weekend={summary[level]['weekend']:.1f}h")

# GRAPH 1: Daily Screen Time by Addiction Level

avg_screen = df.groupby('addiction_level')['daily_screen_time_hours'].mean().reindex(addiction_order)

avg_screen.plot(kind='bar', figsize=(8, 5), color=['#a8d8a8', '#f4a261', '#e63946'], width=0.5)
plt.title('Average Daily Screen Time by Addiction Level', fontsize=13)
plt.xlabel('Addiction Level')
plt.ylabel('Avg Daily Screen Time (hours)')
plt.xticks(rotation=0)
plt.ylim(4, 10)
plt.tight_layout()
plt.savefig('fig1_screentime_addiction.png')
plt.show()

# GRAPH 2: Social Media Hours by Addiction Level

avg_social = df.groupby('addiction_level')['social_media_hours'].mean().reindex(addiction_order)

avg_social.plot(kind='bar', figsize=(8, 5), color=['#a8d8a8', '#f4a261', '#e63946'], width=0.5)
plt.title('Average Social Media Hours by Addiction Level', fontsize=13)
plt.xlabel('Addiction Level')
plt.ylabel('Avg Social Media Hours per Day')
plt.xticks(rotation=0)
plt.ylim(1.5, 4.5)
plt.tight_layout()
plt.savefig('fig2_socialmedia_addiction.png')
plt.show()

# GRAPH 3: Weekend Screen Time by Addiction Level

avg_weekend = df.groupby('addiction_level')['weekend_screen_time'].mean().reindex(addiction_order)

avg_weekend.plot(kind='bar', figsize=(8, 5), color=['#a8d8a8', '#f4a261', '#e63946'], width=0.5)
plt.title('Average Weekend Screen Time by Addiction Level', fontsize=13)
plt.xlabel('Addiction Level')
plt.ylabel('Avg Weekend Screen Time (hours)')
plt.xticks(rotation=0)
plt.ylim(5, 12)
plt.tight_layout()
plt.savefig('fig3_weekend_addiction.png')
plt.show()

# GRAPH 4: Addiction Level Breakdown by Age Group

age_addiction = pd.crosstab(df['age_group'], df['addiction_level'], normalize='index') * 100
age_addiction = age_addiction[addiction_order].reset_index()

age_addiction_melted = age_addiction.melt(id_vars='age_group', var_name='addiction_level', value_name='percentage')

plt.figure(figsize=(9, 5))
sns.barplot(data=age_addiction_melted, x='age_group', y='percentage', hue='addiction_level', hue_order=addiction_order, palette=['#a8d8a8', '#f4a261', '#e63946'])
plt.title('Addiction Level by Age Group (%)', fontsize=13)
plt.xlabel('Age Group')
plt.ylabel('Percentage of Users (%)')
plt.legend(title='Addiction Level')
plt.ylim(0, 65)
plt.tight_layout()
plt.savefig('fig4_age_addiction.png')
plt.show()

#Graph 5: Boxplot -- Screen Time spread across addiction levels

plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='addiction_level', y='daily_screen_time_hours', order=addiction_order, palette=['#a8d8a8', '#f4a261', '#e63946'], width=0.5)
plt.title('Screen Time Distribution by Addiction Level', fontsize=13)
plt.xlabel('Addiction Level')
plt.ylabel('Daily Screen Time (hours)')
plt.tight_layout()
plt.savefig('fig5_boxplot_screentime.png')
plt.show()

#Graph 6: Correlation Heatmap

numeric_cols = ['age', 'daily_screen_time_hours', 'social_media_hours', 'gaming_hours', 'sleep_hours', 'weekend_screen_time']

plt.figure(figsize=(8, 6))
sns.heatmap(df[numeric_cols].corr(), annot=True, fmt='.2f', cmap='coolwarm', center=0, linewidths=0.5)
plt.title('Correlation Between Numeric Features', fontsize=13)
plt.tight_layout()
plt.savefig('fig6_heatmap.png')
plt.show()

#Graph 7: Relationships between all numeric features

cols = ['social_media_hours', 'daily_screen_time_hours', 'sleep_hours', 'gaming_hours', 'addiction_level']

sns.pairplot(df[cols].sample(500, random_state=1), hue='addiction_level', hue_order=addiction_order, palette=['#a8d8a8', '#f4a261', '#e63946'])
plt.suptitle('Pairplot of Usage Features by Addiction Level', y=1.02, fontsize=13)
plt.savefig('fig6_pairplot.png')
plt.show()