import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
#import matplotlib.pyplot as plt
from modulos.canvas import fish_builder



df = pd.read_csv('resources/databases/fish_data.csv')
            ## ../resources/databases/Informacionvuelos.csv
df_numeric = df[['length', 'weight', 'w_l_ratio']].dropna()

scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_numeric)

kmeans = KMeans(n_clusters=5, random_state=42)
kmeans.fit(df_scaled)

df_clean = df.loc[df_numeric.index]
df_clean['Cluster'] = kmeans.labels_
#print(df_clean.head())
#
#plt.scatter(df_clean['species'], df_clean['weight'], c=df_clean['Cluster'], cmap='viridis')
#plt.xlabel('species')
#plt.ylabel('weight')
#plt.title('Fish clustering by w_l_ratio')
#plt.colorbar(label='Cluster')
#plt.show()

fish_canva = fish_builder((df_clean['weight'].min(),df_clean['weight'].max()), df_clean)

