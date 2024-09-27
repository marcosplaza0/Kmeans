import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

data = {
    'Cliente': ['Cliente1', 'Cliente2', 'Cliente3', 'Cliente4', 'Cliente5', 'Cliente6', 'Cliente7', 
                'Cliente8', 'Cliente9', 'Cliente10', 'Cliente11', 'Cliente12', 'Cliente13', 'Cliente14', 'Cliente15'],
    'Frecuencia_Compra': [10, 5, 15, 3, 7, 20, 25, 8, 12, 30, 2, 6, 17, 22, 27],
    'Valor_Gastado': [1000, 500, 1500, 300, 700, 2000, 2500, 900, 1200, 3000, 250, 600, 1800, 2200, 2700],
    'Num_Productos': [50, 25, 75, 15, 35, 100, 120, 45, 60, 130, 10, 30, 80, 110, 140]
}

df = pd.DataFrame(data)

X = df[['Frecuencia_Compra', 'Valor_Gastado', 'Num_Productos']]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Aplicar K-means con 3 clústeres
kmeans = KMeans(n_clusters=3, random_state=0)
df['Cluster'] = kmeans.fit_predict(X_scaled)

plt.figure(figsize=(10, 6))
plt.scatter(X['Num_Productos'], X['Valor_Gastado'], c=df['Cluster'], cmap='viridis', s=100)
plt.xlabel('Frecuencia de Compra')
plt.ylabel('Valor Gastado')
plt.title('Segmentación de Clientes basada en Comportamiento de Compra')
plt.grid(True)
plt.show()


