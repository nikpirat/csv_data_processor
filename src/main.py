import pandas as pd
from src.data_loader import load_data
from src.data_cleaner import clean_data
from src.statistics import calculate_statistics, save_statistics
from src.visualizer import plot_histogram, plot_scatter

def main():
    # Load the data
    data = load_data("../data/raw_data.csv")
    if data is None:
        return

    # Clean the data
    cleaned_data = clean_data(data)

    # Calculate statistics
    stats = calculate_statistics(cleaned_data)
    save_statistics(stats, "../output/statistics.txt")

    # Plot histogram for 'Salary' column
    plot_histogram(cleaned_data, "Salary", "../output/plots/salary_histogram.png")

    # Plot scatter plot for 'Salary' vs 'Age'
    plot_scatter(cleaned_data, "Salary", "Age", "../output/plots/salary_age_scatter.png")

if __name__ == "__main__":
    main()
