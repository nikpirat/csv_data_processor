import matplotlib.pyplot as plt

def plot_histogram(data, column_name, output_path):
    """Plot a histogram for the given column."""
    # Check if the column exists in the DataFrame
    if column_name not in data.columns:
        print(f"Error: Column '{column_name}' not found in data.")
        return

    # Plotting the histogram
    plt.hist(data[column_name], bins=30, color='blue', edgecolor='black')
    plt.title(f"Histogram of {column_name}")
    plt.xlabel(column_name)
    plt.ylabel("Frequency")
    plt.savefig(output_path)
    plt.close()
    print(f"Histogram saved to {output_path}")


def plot_scatter(data, x_column, y_column, output_path):
    """Plot a scatter plot for the given columns."""

    # Check if the columns exist in the DataFrame
    if x_column not in data.columns or y_column not in data.columns:
        print(f"Error: One or both columns '{x_column}' or '{y_column}' not found in data.")
        return

    # Plotting the scatter plot
    plt.scatter(data[x_column], data[y_column], color='blue', edgecolor='black', alpha=0.7)

    plt.title(f"Scatter Plot: {x_column} vs {y_column}")
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.grid(True)
    plt.savefig(output_path)
    plt.close()
    print(f"Scatter plot saved to {output_path}")