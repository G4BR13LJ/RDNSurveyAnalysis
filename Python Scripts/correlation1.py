import pandas as pd
import matplotlib.pyplot as plt

file_path = "SurveyResponses.csv"
df = pd.read_csv(file_path)

filtered_df = df[df['Have you ever contacted a non-profit to determine whether you qualify for \ngovernment grants?'] == 'Yes']

# Correlations
correlations = {
    "Is it clear RDN aids unhoused individuals": 0.43,
    "Trust non-profit with personal info": 0.71,
    "Lived in rural community in the last 6 months": 0.57
}

# Extract questions and correlation values
questions = list(correlations.keys())
values = list(correlations.values())

# Plotting
plt.figure(figsize=(12, 8))  # Increase figure size
bars = plt.barh(questions, values, color='skyblue')
plt.xlabel('Correlation Values')
plt.ylabel('Questions')
plt.title("Likelihood of answering 'Yes' to questions, \ngiven the respondent has contacted a non-profit", fontsize=16)
plt.xlim(0, 1)

# Add actual values next to each bar
for bar, value in zip(bars, values):
    plt.text(bar.get_width() + 0.01, bar.get_y() + bar.get_height() / 2, f'{value:.2f}', va='center', fontsize=12)

plt.tight_layout()

# Show the plot
plt.show()








columns =["Have you ever contacted a non-profit to determine whether you qualify for \ngovernment grants?",
          "Are you employed at the current moment? (self-employed, contractor, etc.)",
          "Do you trust a non-profit organization with personal information more than a corporate organization?",
          "Have you lived in a rural community in the last 6 months"]


# Extract relevant columns
subset_df = df[columns]

# Create a cross-tabulation (contingency table) between the two columns
cross_tab = pd.crosstab(subset_df[columns[0]], subset_df[columns[2]])

# Display the cross-tabulation
print("Cross-Tabulation:")
print(cross_tab)

# Calculate the correlation between the two columns
correlation_value = cross_tab.loc['Yes', 'No'] / (cross_tab.loc['Yes', 'No'] + cross_tab.loc['No', 'No'])

# Display the correlation value
print(f"\nCorrelation Value: {correlation_value}")