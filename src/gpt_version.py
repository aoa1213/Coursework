import pandas as pd

def explore_data(filename):
    # Step 1: Load the dataset
    data = pd.read_csv(filename, encoding='Windows-1252')
    
    # Step 2: Display the first few rows of the dataset
    print("First 5 rows of the dataset:")
    print(data.head(), "\n")
    
    # Step 3: Check the size of the dataset (rows and columns)
    print(f"Size of the dataset: {data.shape[0]} rows, {data.shape[1]} columns\n")
    
    # Step 4: Show the column names and their data types
    print("Column names and their data types:")
    print(data.dtypes, "\n")
    
    # Step 5: Check for missing values
    missing_values = data.isnull().sum()
    print("Missing values in each column:")
    print(missing_values[missing_values > 0], "\n")
    
    # Step 6: Generate summary statistics for numerical columns
    print("Summary statistics for numerical columns:")
    print(data.describe(), "\n")
    
    # Step 7: Check unique values for categorical columns
    print("Unique values in categorical columns:")
    categorical_columns = data.select_dtypes(include=['object']).columns
    for col in categorical_columns:
        print(f"Column: {col}, Unique Values: {data[col].nunique()}")
        print(f"Sample values from {col}: {data[col].unique()[:5]}", "\n")
    
    # Step 8: Explore the distribution of numerical columns
    print("Distribution of numerical columns:")
    for col in data.select_dtypes(include=['float64', 'int64']).columns:
        print(f"Column: {col}")
        print(f"Mean: {data[col].mean()}, Median: {data[col].median()}, Std Dev: {data[col].std()}")
        print(f"Min: {data[col].min()}, Max: {data[col].max()}", "\n")
    
    # Step 9: Check for potential data quality issues (e.g., outliers, inconsistent categories)
    print("Checking for potential data quality issues:")
    
    # Example: Check for outliers using IQR (Interquartile Range)
    for col in data.select_dtypes(include=['float64', 'int64']).columns:
        Q1 = data[col].quantile(0.25)
        Q3 = data[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers = data[(data[col] < lower_bound) | (data[col] > upper_bound)]
        print(f"Outliers in {col}: {outliers.shape[0]} rows")

    # # Example: Check for inconsistent categories in categorical columns
    # for col in categorical_columns:
    #     if data[col].nunique() < 20:  # Only print if the number of unique values is small
    #         print(f"Inconsistent categories in {col}:")
    #         print(data[col].value_counts(), "\n")
    
    # # Step 10: Display correlations (optional, for numerical columns)
    # print("Correlation matrix for numerical columns:")
    # print(data.corr(), "\n")

# Call the function with the path to your CSV file
explore_data('Stops_LDS_Extract_24Months.csv')

