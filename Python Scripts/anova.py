import pandas as pd
from scipy.stats import f_oneway

file_path = "SurveyResponses.csv"
df = pd.read_csv(file_path)

# Numeric columns for boxplots
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

# Categorical column for grouping
categorical_column = 'Have you lived in a rural community in the last 6 months'

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

# Extract unique groups from the categorical column
groups = df[categorical_column].unique()

# Perform one-way ANOVA for each numeric column
for numeric_column, short_numeric_column in zip(numeric_columns, short_numeric_columns):
    print(f"\nANOVA for {short_numeric_column} grouped by Rural identification:")
    for group in groups:
        group_data = df[df[categorical_column] == group][numeric_column]
        print(f"Group '{group}': Mean = {group_data.mean()}, Variance = {group_data.var()}")

    # Perform one-way ANOVA
    statistic, p_value = f_oneway(*[df[df[categorical_column] == group][numeric_column] for group in groups])

    # Output the results
    print("ANOVA Statistic:", statistic)
    print("P-value:", p_value)

    # Check the significance of the p-value
    alpha = 0.05
    if p_value < alpha:
        print("Reject the null hypothesis; there are significant differences between groups.")
    else:
        print("Fail to reject the null hypothesis; there are no significant differences between groups.")
