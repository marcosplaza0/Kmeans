import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt



df = pd.read_csv('fish_data.csv')
df_numeric = df[['length', 'weight']].dropna()

scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_numeric)

kmeans = KMeans(n_clusters=5, random_state=42)
kmeans.fit(df_scaled)

centroids = kmeans.cluster_centers_
df_clean = df.loc[df_numeric.index]
df_clean['Cluster'] = kmeans.labels_

plt.scatter( df_clean['weight'], df_clean['species'], c=df_clean['Cluster'], cmap='viridis')
plt.ylabel('species')
plt.xlabel('weight')
plt.title('Fish clustering by w_l_ratio')
plt.colorbar(label='Cluster')
plt.show()

