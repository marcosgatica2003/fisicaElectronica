import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Datos
I_H = np.array([1.77, 1.69, 1.64, 1.58, 1.51, 1.44, 1.37, 1.27])
U = np.array([300, 280.6, 260, 240.2, 220.2, 200, 180, 160.2])
factor = 7.584 * (10**-4)

# Calcular U usando la fórmula 2U = (r * I_H * factor)^2
i_h = (0.045 * I_H * factor)**2
u = 2 * U

# Realizar la regresión lineal
slope, intercept, r_value, p_value, std_err = linregress(i_h, u)

# Obtener los valores ajustados
U_fit = slope * i_h + intercept

# Imprimir la pendiente
print(f'Pendiente: {slope} C/Kg')

# Graficar los datos y la curva ajustada
plt.plot(i_h, u, 'bo', label='Datos experimentales')
plt.plot(i_h, U_fit, 'r-', label='Ajuste lineal')
plt.xlabel('(r *B)^2')
plt.ylabel('2U (V)')
plt.title('2U en función de (r *B)^2 r = 0.045 m')
plt.grid(False)
plt.legend()
plt.show()
