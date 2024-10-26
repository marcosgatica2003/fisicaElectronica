import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Datos del segundo orden
data_2nd_order = {
    'Color': ['Amarillo', 'Verde', 'Azul', 'Violeta', 'Ultravioleta'],
    'Frecuencia': [-8.184, -7.400, -6.849, -5.890, -5.190],
    'Energía': [234.3, 302.5, 1000, 1800, 800]
}

# Crear DataFrame
df_2nd_order = pd.DataFrame(data_2nd_order)

# Realizar regresión lineal
x = df_2nd_order['Frecuencia']
y = df_2nd_order['Energía']
coefficients = np.polyfit(x, y, 1)
polynomial = np.poly1d(coefficients)
trendline = polynomial(x)

# Mostrar la pendiente
pendiente = coefficients[0]
print(f'La pendiente de la recta de tendencia es: {pendiente} 10^14 Hz') # la undad de medida de la

# Crear gráfico
plt.figure(figsize=(10, 5))
plt.scatter(x, y, marker='o', label='Datos')
plt.plot(x, y, linestyle='-', color='blue', label='Conexión de puntos')  # Conectar los puntos
plt.plot(x, trendline, color='red', label='Recta de tendencia')

# Añadir la pendiente al gráfico
plt.title('Segundo Orden')
plt.xlabel('Frecuencia ($\\times 10^{14}$ Hz)')
plt.ylabel('Energía $V_{0}$ (mV)')
plt.grid(False)  # Desactivar la cuadrícula
plt.legend()

# Ajustar el tamaño de las etiquetas de los ejes
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Mostrar el gráfico
plt.tight_layout()
plt.show()
