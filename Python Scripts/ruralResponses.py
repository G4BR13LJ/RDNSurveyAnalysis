import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict

file_path = "SurveyResponses.csv"
df = pd.read_csv(file_path)

# Assuming df is your DataFrame containing the survey responses

# Filter the DataFrame based on the condition
filtered_df = df[df['Have you taken any Computer Science classes?'] == 'Yes']

# Specify the columns of interest
columns = ["How important is it that website theme colours match a brand's logo colours?",
           "Are you more likely to browse a website with colour throughout its pages",
           "How likely are you to stay on RDN website if it is hard to navigate if it can \npotentially help you with funding and income assistance?",
           "Are you more likely to open a navigation menu if it is discreet and in the top left of a screen?",
           "How does the following feature rank for you on user-friendliness:\nScreen navigation options always stay at the top of the screen (If you scroll down, there is always a bar on the top of the screen)",
           "How do home page videos affect your perception of a website?"]

# Shorten column names for better axis labels
shortened_columns = [
    "Brand Theme Colors Used on Site Pages",
    "Colorful Pages Importance",
    "Retention for Hard Navigation",
    "Discreet Menu in Top Left",
    "Top Screen Nav Bar Always Available",
    "Home Page Videos Importance"]

# Create a dictionary to map original column names to shortened names
column_mapping = dict(zip(columns, shortened_columns))

# Create an empty dictionary to store mean values
mean_values = {}

# Calculate mean values for each column
for column_name in columns:
    mean_values[column_name] = filtered_df[column_name].mean()

# Sort columns based on mean values in descending order
sorted_columns = sorted(columns, key=lambda x: mean_values[x], reverse=True)

# Use the mapping to get the corresponding shortened names
sorted_shortened_columns = [column_mapping[column] for column in sorted_columns]

# Plotting
plt.figure(figsize=(10, 6))
bars = plt.bar(sorted_shortened_columns, [mean_values[column] for column in sorted_columns], color='skyblue')
plt.xlabel('Questions')
plt.ylabel('Mean Values')
plt.title('Mean Values for Survey Questions (For CS students)')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability

# Add actual values on top of each bar
for bar, value in zip(bars, [mean_values[column] for column in sorted_columns]):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.01, f'{value:.2f}', ha='center', va='bottom')

plt.tight_layout()

# Show the plot
plt.show()

