import os 
import pandas as pd
from sklearn.preprocessing import StandardScaler



def scale_data(df):
    features = ['sepal.length', 'sepal.width', 'petal.length', 'petal.width']
    temp = df[features]
    scaler = StandardScaler()
    temp = scaler.fit_transform(temp)
    df[features] = temp
    return df


if __name__ == '__main__':
    # Load the data
    df = pd.read_csv('data/prepared/cleaned_iris.csv')

    # Scale the data
    df = scale_data(df)

    # Save the data
    if not os.path.exists(os.path.join('data','prepared')):
        os.makedirs(os.path.join('data','prepared'),exist_ok=True)
    df.to_csv(os.path.join('data','prepared','prepared_iris.csv'), index=False)