import pandas as pd

df = pd.read_csv('../../data/synthetic_data.csv')
df['pace'] = df['duration_min'] / df['distance_km']
print(df[['user_id', 'date', 'pace']].head())