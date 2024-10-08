import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from modulos.canvas import fish_builder

df = pd.read_csv('resources/databases/fish_data.csv')
df_numeric = df[['length', 'weight']].dropna()

scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_numeric)

kmeans = KMeans(n_clusters=5, random_state=42)
kmeans.fit(df_scaled)

df_clean = df.loc[df_numeric.index]
df_clean['Cluster'] = kmeans.labels_

fish_canva = fish_builder((df_clean['weight'].min(),df_clean['weight'].max()), df_clean)

