import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict

file_path = "SurveyResponses.csv"
df = pd.read_csv(file_path)

# Print column names
print("Column Names:")
# print(df.columns)

# Print unique values and their counts for each column
for column in df.columns:
    print(f"\nUnique values and counts for column '{column}':")
    print(df[column].value_counts())

color_engagement_counts = df['Is it clear from browsing their homepage that RDN heavily works to aid unhoused individuals '].value_counts()
color_engagement_counts.plot(kind='bar', rot=0)
plt.xlabel('Response')
plt.ylabel('Count')
plt.title('Is it clear RDN helps fight homelessness')
plt.show()

indigenous_color_counts = df['Which of the following colours, most identify with indigenous culture?'].value_counts()
indigenous_color_counts.plot(kind='bar', rot=0)
plt.xlabel('Color')
plt.ylabel('Count')
plt.title('Distribution of Responses for Indigenous Colors')
plt.show()


contact_nonprofit_counts = df['Have you ever contacted a non-profit to determine whether you qualify for \ngovernment grants?'].value_counts()
contact_nonprofit_counts.plot(kind='bar', rot=0)
plt.xlabel('Response')
plt.ylabel('Count')
plt.title('Distribution of Responses for Contacting Non-Profit')
plt.show()

social_media_relevance = df['How relevant is a social media presence to the validity of brand?']
social_media_counts = social_media_relevance.value_counts()

# Bar plot
social_media_counts.plot(kind='bar', rot=0)
plt.xlabel('Relevance Level')
plt.ylabel('Count')
plt.title('Distribution of Relevance Levels for Social Media Presence')
plt.show()

quality_influence = df['Does the overall quality and ease of use of a website influence the amount of time you spend on that website?']
quality_counts = quality_influence.value_counts()

# Bar plot
quality_counts.plot(kind='bar', rot=0)
plt.xlabel('Response')
plt.ylabel('Count')
plt.title('Distribution of Responses for Influence of Website Quality on Time Spent')
plt.show()

# Map 'Yes' to 1 and 'No' to 0
df['Rural Community'] = df['Have you lived in a rural community in the last 6 months'].map({'Yes': 1, 'No': 0})
df['Website Influence'] = df['Does the overall quality and ease of use of a website influence the amount of time you spend on that website?'].map({'Yes': 1, 'No': 0})

# Calculate correlation matrix
correlation_matrix = df[['Rural Community', 'How likely would one be to stay engaged on this website for more than one minute? Link to website', 'How relevant is a social media presence to the validity of brand?', 'Website Influence']].corr()

# Create a heatmap
plt.figure(figsize=(12, 10))
heatmap = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=.5)

# Adjust layout without tight_layout
plt.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.2)

# Center the labels within each square
heatmap.set_xticks([tick + 0.5 for tick in range(len(correlation_matrix.columns))])
heatmap.set_xticklabels(['Rural Comm.', 'Engagement', 'Social Media', 'Web Influence'])

heatmap.set_yticks([tick + 0.5 for tick in range(len(correlation_matrix.columns))])
heatmap.set_yticklabels(['Rural Comm.', 'Engagement', 'Social Media', 'Web Influence'])

plt.title('Correlation Heatmap')
plt.show()

