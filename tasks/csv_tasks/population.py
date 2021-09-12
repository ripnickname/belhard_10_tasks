"""
Написать функцию max_delta, в которой будет происходить чтение csv
файла world_population.csv и функцию должна возвращать год, в котором
наибольший процент прироста населения.
"""


import pandas as pd

def max_delta():
    df = pd.read_csv('world_population.csv')
    best_percentage = df['ChangePerc'].max()
    df_percent = df[df['ChangePerc'] == best_percentage]
    df_year = df_percent['Year']
    print(df_year)


if __name__ == '__main__':
    max_delta()


