import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "SurveyResponses.csv"
df = pd.read_csv(file_path)

# Numeric columns for boxplots
# numeric_columns = [
#     'How likely would one be to stay engaged on this website for more than one minute? Link to website',
#     'How relevant is a social media presence to the validity of brand?',
#     'How do home page videos affect your perception of a website?',
#     "Are you more likely to browse a website with colour throughout its pages",
#     "How likely are you to stay on RDN website if it is hard to navigate if it can \npotentially help you with funding and income assistance?",
#     "How does the following feature rank for you on user-friendliness:\nScreen navigation options always stay at the top of the screen (If you scroll down, there is always a bar on the top of the screen)",
#     "Are you more likely to open a navigation menu if it is discreet and in the top left of a screen?",
#     "How important is it that website theme colours match a brand's logo colours?"
# ]
numeric_columns = [
    'How likely would one be to stay engaged on this website for more than one minute? Link to website',
    'How relevant is a social media presence to the validity of brand?',
    'How do home page videos affect your perception of a website?',
    "Are you more likely to browse a website with colour throughout its pages",
    "How likely are you to stay on RDN website if it is hard to navigate if it can \npotentially help you with funding and income assistance?",
    "How does the following feature rank for you on user-friendliness:\nScreen navigation options always stay at the top of the screen (If you scroll down, there is always a bar on the top of the screen)",
    "Are you more likely to open a navigation menu if it is discreet and in the top left of a screen?",
    "How important is it that website theme colours match a brand's logo colours?"
]

# Categorical columns for grouping
categorical_columns = [
    'Is it clear from browsing their homepage that RDN heavily works to aid unhoused individuals ',
]

# Shortened versions for plots
short_numeric_columns = [
    'Engagement',
    'Social Media',
    'Home Page Vids',
    'Color importance',
    'Income help',
    'Nav bar access',
    'Top left nav bar',
    'Brand color usage'
]

# Shortened versions for plots
short_categorical_columns = [
    'Is it clear that RDN helps to homelessness'
]

# Create boxplots
for numeric_column, short_numeric_column in zip(numeric_columns, short_numeric_columns):
    for categorical_column, short_categorical_column in zip(categorical_columns, short_categorical_columns):
        plt.figure(figsize=(12, 6))
        sns.boxplot(data=df, x=categorical_column, y=numeric_column)
        plt.title(f'Box Plot of {short_numeric_column} by {short_categorical_column}')
        plt.xlabel(short_categorical_column)
        plt.ylabel(short_numeric_column)
        plt.show()


# # Create correlation heatmap with shortened names
# correlation_matrix = df[numeric_columns].corr()
# correlation_matrix = correlation_matrix.rename(
#     columns=dict(zip(numeric_columns, short_numeric_columns)),
#     index=dict(zip(numeric_columns, short_numeric_columns))
# )
#
# # Increase the figure size
# plt.figure(figsize=(14, 10))
#
# sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
# plt.title('Correlation Heatmap of Numeric Columns')
#
# # Rotate x and y axis labels for better visibility
# plt.xticks(rotation=45, ha='right')
# plt.yticks(rotation=0)
#
# plt.show()
