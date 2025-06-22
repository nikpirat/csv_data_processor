import pandas as pd
import numpy as np


def calculate_statistics(data):
    """Calculate basic statistics of the dataset."""
    stats = {}

    # Separate numeric and non-numeric columns
    numeric_data = data.select_dtypes(include=[np.number])  # Only numeric columns
    non_numeric_data = data.select_dtypes(exclude=[np.number])  # Non-numeric columns

    # For numeric columns, calculate mean, median, etc.
    stats['mean'] = numeric_data.mean() # Calculates the mean (average) value of each numeric column.
    stats['median'] = numeric_data.median() # Computes the median (middle value) for each numeric column.
    stats['mode'] = numeric_data.mode().iloc[0]  # .mode() returns the most frequent value(s) for each column. Since a column may have multiple modes, iloc[0] gets the first mode.
    stats['std_dev'] = numeric_data.std() # Calculates the standard deviation for each numeric column — a measure of how spread out the values are.
    stats['variance'] = numeric_data.var() # Computes the variance of each numeric column — it's the square of the standard deviation.

    # For non-numeric columns, calculate mode and counts
    stats['mode_non_numeric'] = non_numeric_data.mode().iloc[0] # Finds the most frequent (mode) categorical value in each non-numeric column.
    stats['count_non_numeric'] = non_numeric_data.count() # Returns the count of non-null (non-missing) entries in each non-numeric column.

    # Correlations (only for numeric columns)
    stats['correlation'] = numeric_data.corr() # Computes the Pearson correlation coefficient between numeric columns. This value ranges from -1 (strong negative correlation) to 1 (strong positive correlation).

    return stats


def save_statistics(stats, output_path):
    """Save statistical results to a text file."""
    with open(output_path, 'w') as file:
        for key, value in stats.items():
            file.write(f"{key}:\n{value}\n\n")
    print(f"Statistics saved to {output_path}")
