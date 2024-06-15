import os
import pandas as pd


def clean_data(df):
    """
    This function cleans the data by removing rows with missing values and
    converting the 'variety' column to a int.
    """
    # Drop rows with missing values
    df = df.dropna()

    # Convert the 'variety' column to a int
    df['variety'] = df['variety'].map({'Setosa': 0, 'Versicolor': 1, 'Virginica': 2})
    
    return df 

if __name__ == '__main__':
    print('Cleaning data...')
    # Load the data
    df = pd.read_csv('data/raw/iris.csv')

    # Clean the data
    df = clean_data(df)

    # Save the data
    if not os.path.exists(os.path.join('data','prepared')):
        os.makedirs(os.path.join('data','prepared'),exist_ok=True)
    df.to_csv(os.path.join('data','prepared','cleaned_iris.csv'), index=False)
