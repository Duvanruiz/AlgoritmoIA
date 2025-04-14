import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns

# Simular datos
data = {
    'Latitud': [4.651, 4.658, 4.655, 4.670, 4.661, 4.663, 4.649, 4.672],
    'Longitud': [-74.091, -74.095, -74.100, -74.085, -74.090, -74.080, -74.101, -74.088],
    'Pasajeros_Por_Hora': [230, 115, 300, 450, 200, 320, 110, 400],
    'Tiempo_Espera_Min': [12, 8, 15, 20, 10, 17, 7, 18],
    'Día_Semana': ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Lunes', 'Martes', 'Viernes']
}

df = pd.DataFrame(data)

# Codificar el día de la semana (opcional)
le = LabelEncoder()
df['Día_Semana'] = le.fit_transform(df['Día_Semana'])

# Seleccionar características numéricas para clustering
X = df[['Latitud', 'Longitud', 'Pasajeros_Por_Hora', 'Tiempo_Espera_Min']]

# Aplicar KMeans
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(X)

# Visualización
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Longitud', y='Latitud', hue='Cluster', palette='Set2', s=100)
plt.title('Agrupamiento de zonas según uso del transporte')
plt.xlabel('Longitud')
plt.ylabel('Latitud')
plt.grid(True)
plt.show()
