def clean_data(data):
    """Clean the data by handling missing values and data types."""
    # Drop rows with missing values
    data = data.dropna()

    # Optional: Convert columns to appropriate data types
    # data['column_name'] = data['column_name'].astype(int)

    print("Data cleaned successfully.")
    return data
