import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict

file_path = "SurveyResponses.csv"
df = pd.read_csv(file_path)

# Print column names
print("Column Names:")
# print(df.columns)

# Create a horizontal bar plot
plt.figure(figsize=(10, 6))
color_engagement_counts = df['Which of the following resources do you consider of highest importance?'].value_counts()
color_engagement_counts.plot(kind='barh')  # Use barh for horizontal bar plot
plt.xlabel('Count')
plt.ylabel('Response')
plt.title('Distribution for Important Resources')
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()