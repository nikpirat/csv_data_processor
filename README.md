# CSV Data Processor

This Python project reads a CSV file, processes it, performs statistical analysis, and visualizes the data.

**Loads and processes CSV data.**
Performs statistical analysis (like mean, median, mode, standard deviation).
Generates data visualizations (like histograms, bar plots, scatter plots) using Matplotlib.
Outputs the processed data and statistics for review.

**Data Loading and Preprocessing**
Read CSV data using Pandas.
Clean and preprocess the data (e.g., handling missing values, data types, outliers).

**Statistical Analysis**
Use NumPy and Pandas to calculate basic statistics:
Mean, Median, Mode
Standard Deviation, Variance
Correlations

**Data Visualization**
Use Matplotlib to visualize the data:
Line plots, histograms, and box plots.
Scatter plots for bivariate analysis.
Heatmaps for correlation matrices.

**Export Results**
Export the processed data or statistics into a CSV or Excel file for further use or sharing.

## Setup

1. Clone the repository
2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt

3. Place your CSV data in the data/ directory.
4. Run the program:
   ```bash
   python src/main.py

### 5. **Running the Project**
1. Save the CSV data file (e.g., `raw_data.csv`) in the `data/` folder.
2. Run the project:

    ```bash
    python src/main.py

After running the program, you should see the processed data, statistical analysis, and visualizations in the output/ directory.