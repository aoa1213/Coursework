import pandas as pd


def explore_datafile(filename):
    # Step 1: Read the dataset
    df = pd.read_csv(f"{filename}", encoding='Windows-1252')

    # Step 2: Check the size of the dataset (rows and columns)
    print(f"Size of the dataset: {df.shape[0]} rows, {df.shape[1]} columns\n")

    # Step 3: Print out the first 5 rows
    print("The first 5 rows of the dataframe are \n")
    print(df.head(5))

    # Step 4: Show the general information of dataframe
    print(df.info(), "\n")

    # Step 5: Generate summary statistics for numeric columns
    print("Summary statistics for numerical columns:")
    print(df.describe(), "\n")

    # Step 7: Check unique values for each columns
    print("Unique values in each columns:")
    categorical_columns = df.select_dtypes(include=['object']).columns
    # datatype of int64 or float64 is not included since there are too many different value
    for col in categorical_columns:
        print(f"Column: {col}, Unique Values: {df[col].nunique()}")
        print(f"Some unique values from {col}: {df[col].unique()[:5]}", "\n")

    # Define the extreme value



# def data_preparation(df):
#     # Step 5: Delte the column not needed
#     column_name_to_drop =["Borough Code","Officer OCU"]
#     df = df.drop(column_name_to_drop, axis=1)
#     print("New Column names and their data types:")
#     print(df.dtypes, "\n")

#     #Step 6: Check column of type float64 for missing values and fill the missing value before convert into int
#     missing_values = df.isnull().sum()
#     print("Missing values in each column:")
#     print(missing_values[missing_values > 0], "\n")
#     for column,dtype in df.dtypes.items():
#         if dtype == 'float64':
#             missing_values = df[column].isnull().sum()
#             if missing_values>0:
#                 print(f"Missing values in {column} column:{missing_values}")
#                 mean_value = df[column].mean()  # calculate the mean value
#                 #df[column] = df[column].fillna(mean_value, inplace=True)  # replace empty value with mean value
#                 df.fillna({'Age': mean_value}, inplace=True) # replace empty value with mean value


#     # Step 7: Convert the float64 type into int64
#     print(df.dtypes.items())
#     for column, dtype in df.dtypes.items():
#         if dtype == 'float64':
#             df[column] = df[column].astype('int')
#             print(f"Column: {column}, Data Type: {dtype} is changed to int64")


    # # Step 5: Generate summary statistics for numerical columns
    # print("Summary statistics for numerical columns:")
    # print(df.describe(), "\n")




# def find_min_in_column(filename, column_name):
#     # Step 1: Load the dataset into a pandas DataFrame
#     data = pd.read_csv(filename, encoding='Windows-1252')
    
#     # Step 2: Find the minimum value in the specified column
#     if column_name in data.columns:
#         min_value = data[column_name].min()
#         print(f"Minimum value in column '{column_name}': {min_value}")
        
#         # Step 3: Locate the row index of the minimum value
#         min_row = data[data[column_name] == min_value].index[0]  # First occurrence of the min value
#         print(f"Minimum value {min_value} found at row {min_row} in column '{column_name}'")
#     else:
#         print(f"Column '{column_name}' not found in the dataset.")
#     print(data.iloc[min_row])

if __name__ == "__main__":
    # Filepath of the csv data file
    try:
        explore_datafile("Stops_LDS_Extract_24Months.csv")
        #find_min_in_column("Stops_LDS_Extract_24Months.csv","Age")
    except FileNotFoundError as e:
        print(f"File not found. Please check the file path. Error: {e}")

