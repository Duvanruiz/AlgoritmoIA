import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
import matplotlib.pyplot as plt

# Crear dataset simulado
data = {
    'Hora_Pico': ['Sí', 'No', 'Sí', 'No', 'Sí', 'Sí', 'No', 'No'],
    'Clima': ['Lluvia', 'Soleado', 'Nublado', 'Lluvia', 'Lluvia', 'Soleado', 'Nublado', 'Soleado'],
    'Zona': ['Norte', 'Centro', 'Sur', 'Oeste', 'Centro', 'Norte', 'Sur', 'Centro'],
    'Demanda_Estimada': ['Alta', 'Media', 'Alta', 'Baja', 'Media', 'Alta', 'Baja', 'Media'],
    'Ruta_Saturada': ['Sí', 'No', 'Sí', 'No', 'No', 'Sí', 'No', 'No']
}

df = pd.DataFrame(data)

# Codificar variables categóricas
label_encoders = {}
for column in df.columns:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    label_encoders[column] = le

# Separar características y etiqueta
X = df.drop('Ruta_Saturada', axis=1)
y = df['Ruta_Saturada']

# Separar en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Entrenar modelo de árbol de decisión
clf = DecisionTreeClassifier(criterion='entropy', random_state=42)
clf.fit(X_train, y_train)

# Evaluar modelo
accuracy = clf.score(X_test, y_test)
print(f"Precisión del modelo: {accuracy:.2f}")

# Visualizar el árbol
plt.figure(figsize=(12, 8))
tree.plot_tree(clf, feature_names=X.columns, class_names=label_encoders['Ruta_Saturada'].classes_, filled=True)
plt.show()
