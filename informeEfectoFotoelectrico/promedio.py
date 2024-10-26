import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Datos del primer orden
data_1st_order = {
    'Color': ['Amarillo', 'Verde', 'Azul', 'Violeta', 'Ultravioleta'],
    'Frecuencia (x 10^14 Hz)': [6.636, 6.503, 6.864, 6.649, 6.696],
    'Energía (mV)': [964, 827.4, 1065, 1515, 900]
}

# Crear DataFrame
df_1st_order = pd.DataFrame(data_1st_order)

# Realizar regresión lineal
x_1st = df_1st_order['Frecuencia (x 10^14 Hz)']
y_1st = df_1st_order['Energía (mV)']
coefficients_1st = np.polyfit(x_1st, y_1st, 1)
polynomial_1st = np.poly1d(coefficients_1st)
trendline_1st = polynomial_1st(x_1st)

# Mostrar la pendiente
pendiente_1st = coefficients_1st[0]

# Crear gráfico
plt.figure(figsize=(10, 5))
plt.scatter(x_1st, y_1st, marker='o', label='Datos')
plt.plot(x_1st, trendline_1st, color='red', label='Recta de tendencia')

# Añadir la pendiente al gráfico
plt.title('Primer Orden')
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
