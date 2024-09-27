import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from modulos.canvas import shop_builder


df = pd.read_csv('resources/databases/Customers.csv')

df_numeric = df[['Annual Income ($)', 'Spending Score (1-100)']].dropna()

scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_numeric)

kmeans = KMeans(n_clusters=4, random_state=42)
kmeans.fit(df_scaled)

df_clean = df.loc[df_numeric.index]
df_clean['Cluster'] = kmeans.labels_

shop_canva = shop_builder((df_clean['Annual Income ($)'].min(),df_clean['Annual Income ($)'].max()), df_clean)
