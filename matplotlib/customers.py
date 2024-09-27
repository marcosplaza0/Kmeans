import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt



df = pd.read_csv('customers_data.csv')

df_numeric = df[['Annual Income ($)', 'Spending Score (1-100)']].dropna()

scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_numeric)

kmeans = KMeans(n_clusters=4, random_state=42)
kmeans.fit(df_scaled)

df_clean = df.loc[df_numeric.index]
df_clean['Cluster'] = kmeans.labels_

plt.scatter(df_clean['Annual Income ($)'], df_clean['Spending Score (1-100)'], c=df_clean['Cluster'], cmap='viridis')
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.title('Tienda Cluster')
plt.colorbar(label='Cluster')
plt.show()

