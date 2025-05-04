import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict

file_path = "SurveyResponses.csv"
df = pd.read_csv(file_path)

# Print column names
# print("Column Names:")
# print(df.columns)

# Print unique values and their counts for each column
for column in df.columns:
    print(f"\nUnique values and counts for column '{column}':")
    print(df[column].value_counts())

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

# Calculate and print the mean for the specified column
for column_name in columns:
    column_mean = df[column_name].mean()
    print(f"Mean for question: '{column_name}': {column_mean}\n")

# Create a dictionary to map original column names to shortened names
column_mapping = dict(zip(columns, shortened_columns))

# Create an empty dictionary to store mean values
mean_values = {}

# Calculate mean values for each column
for column_name in columns:
    mean_values[column_name] = df[column_name].mean()

# Sort columns based on mean values in descending order
sorted_columns = sorted(columns, key=lambda x: mean_values[x], reverse=True)

# Use the mapping to get the corresponding shortened names
sorted_shortened_columns = [column_mapping[column] for column in sorted_columns]

# Plotting
plt.figure(figsize=(10, 6))
bars = plt.bar(sorted_shortened_columns, [mean_values[column] for column in sorted_columns], color='skyblue')
plt.xlabel('Questions')
plt.ylabel('Mean Values')
plt.title('Mean Values for Survey Questions (Ordered by Highest Mean)')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability

# Add actual values on top of each bar
for bar, value in zip(bars, [mean_values[column] for column in sorted_columns]):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.01, f'{value:.2f}', ha='center', va='bottom')

plt.tight_layout()

# Show the plot
plt.show()

# Create a dictionary to store the counts
occurrence_counts = defaultdict(int)

# Iterate over each row in the specified column
for entry in df['Which image/images resonates with a website that works with Indigenous communities']:
    # Split the entries in each row
    entries_list = entry.split(', ')

    # Update the counts in the dictionary
    for individual_entry in entries_list:
        occurrence_counts[individual_entry] += 1

# Print the results
print("Response\tOccurrences")
print("------------------------")
for response, count in occurrence_counts.items():
    print(f"{response}\t\t{count}")

# Convert the dictionary to a DataFrame for easier plotting
occurrence_df = pd.DataFrame(list(occurrence_counts.items()), columns=['Response', 'Occurrences'])

# Sort the DataFrame by occurrences in descending order
occurrence_df = occurrence_df.sort_values(by='Occurrences', ascending=False)

# Plotting
plt.figure(figsize=(10, 6))
bars = plt.bar(occurrence_df['Response'], occurrence_df['Occurrences'], color='skyblue')
plt.xlabel('Response')
plt.ylabel('Occurrences')
plt.title('Occurrences for Each Response')
#plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability

# Add actual values on top of each bar
for bar, value in zip(bars, occurrence_df['Occurrences']):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.1, f'{value}', ha='center', va='bottom')

plt.tight_layout()

# Show the plot
plt.show()

