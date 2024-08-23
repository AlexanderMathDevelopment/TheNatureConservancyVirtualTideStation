# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 20:11:45 2024

@author: draja
"""

import matplotlib.pyplot as plt

# Datos de altura de marea para el año 2008
meses = [
    'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto',
    'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
]

# Datos para el año 2008
datos_2008 = [
    1.11, 3.5, 3.5, 0.29, 0.07, -0.73, -1.02, -1.36, -0.54, -0.19, 0.38, 0.45,
    3.57, 0.42, 0.66, 5.11, 5.05, 5.78, 5.82, 5.3, 5.57, 5.3, 3.65, 4.53,
    0.43, 3.99, 4.08, -0.31, -0.87, -1.19, -1.32, -0.7, 0.31, 0.48, 1.1, 1.08,
    4.21, -0.38, -0.39, 5.6, 6.03, 5.95, 5.97, 5.59, 4.17, 4.2, 2.78, 3.95,
    -0.11, 5.09, 5.24, -1.03, -1.19, -0.94, -0.66, 0.46, 0.93, 1.19, 3.5, 1.34,
    3.8, -0.96, -1.07, 6.28, 6.07, 5.39, 5.39, 4.26, 3.24, 2.86, 1.79, 3.63,
    -0.53, 5.95, 6, -1.08, -0.83, 0.09, 0.56, 1.15, 2.84, 1.9, 3.87, 0.5,
    5.35, -0.33, -0.93, 5.71, 5.1, 4.48, 4.14, 2.11, 1.9, 3.54, 0.38, 4.49,
    -0.69, 6.05, 6.02, -0.39, 0.22, 1.3, 1.67, 2.82, 3.46, 0.9, 4.29, -0.43,
    5.76, -0.36, -0.72, 4.05, 4.07, 3.76, 2.97, 3.07, 3.96, 4.39, -0.6, 5.03,
    -0.35, 5.16, 5.05, 0.85, 1.79, 1.55, 1.2, 0.95, 0.36, -0.14, 5.28, -1.09,
    5.71, 0.1, 0.07, 3.93, 4.1, 3.76, 3.47, 3.9, 4.99, 5.09, -1.09, 5.83,
    0.34, 3.52, 3.42, 1.02, 0.39, 0.33, 3.05, 0.12, -0.52, -0.97, 6.03, 0.12,
    4.31, 0.85, 1.17, 4.56, 4.23, 4.32, 0.83, 4.94, 5.74, 5.85, -0.96, 5.94,
    0.54, 4.05, 4.18, 0.04, -0.06, -0.2, 4.47, -0.56, -0.94, -1.09, 5.86, -0.31,
    3.73, 0.13, 0.07, 4.99, 4.86, 4.8, -0.29, -0.18, 5.54, 6.17, 0.49, 5.36,
    0.35, 4.59, 5.08, -0.53, -0.54, -0.36, 5.24, 6.01, -0.06, -0.57, 4.38, 0.96,
    4.65, -1.08, -0.75, 5.46, 5.26, 5.18, -0.6, -0.49, 5.81, 5.32, 1.07, 4.33,
    -0.79, 5.54, 5.12, -0.7, -0.49, -0.36, 5.75, 5.8, -0.12, 0.55, 3.28, 1.09,
    5.12, -1.07, -0.72, 5.62, 5.31, 5.31, -0.61, -0.28, 3.73, 3.87, 1.13, 3.66,
    -1.31, 6.05, 5.7, -0.38, -0.21, -0.17, 5.59, 5.01, 2.88, 1.14, 0.58, 3.93,
    5.84, -0.34, -0.5, 5.19, 4.98, 5.04, -0.13, 0.95, 1.02, 3.95, 4.43, 0.09,
    -0.87, 5.75, 5.48, 0.08, 0.2, 0.33, 5.19, 3.52, 1.07, 0.49, 4.11, 4.21,
    5.99, 5.28, -0.02, 4.33, 4.36, 4.28, 0.3, 0.77, 4.54, 4.63, -0.56, -0.19,
    0.17, 0.52, 4.63, 0.7, 0.84, 0.97, 3.03, 3.86, -0.21, -0.52, 5.03, 4.71,
    5.29, 4.02, 1.67, 3.35, 1.18, 3.52, 0.63, 0.71, 5.28, 5.12, -0.59, -0.43,
    0.91, 0.94, 3.58, 1.54, 3.86, 0.67, 3.86, 4.99, -0.77, -0.84, 5.3, 5.15,
    3.94, 2.67, 1.13, 2.74, 1.19, 4.09, 0.11, 5.46, 5.66, 5.66, -0.26, -0.31,
    1.26, 2.98, 3.18, 1.13, 0.88, -0.08, 4.94, -1.18, -0.75, -0.23, 5.22, 5.36,
    2.85, 0, 1.55, 0.55, 4.33, 5.1, -1.06, 6.05, 5.85, 5.28, 0.18, -0.01,
    1.33, 0, 4.2, 0, -0.32, 0, 5.84, -0.58, 0, 0, 0, 5.17
]

# Convertir los datos en una lista de listas, una por mes
datos_meses = [datos_2008[i:i+12] for i in range(0, len(datos_2008), 12)]

# Graficar los datos
plt.figure(figsize=(14, 8))

for i, datos in enumerate(datos_meses):
    plt.plot(meses, datos, marker='o', linestyle='-', label=f'Dataset {i+1}')

plt.title('Altura de Marea por Mes en 2008')
plt.xlabel('Mes')
plt.ylabel('Altura de Marea')
plt.grid(True)
plt.xticks(rotation=45)
plt.legend(title="Datasets")
plt.tight_layout()
plt.show()
