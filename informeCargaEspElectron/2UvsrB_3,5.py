import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Datos
I_H = np.array([2.25, 2.179, 2.14, 2.03, 1.969, 1.859, 1.77, 1.65])
U = np.array([300.4, 280.5, 260, 240.3, 220.2, 200.2, 180.1, 160.3])
factor = 7.584 * (10**-4)

# Calcular U usando la fórmula 2U = (r * I_H * factor)^2
i_h = (0.035 * I_H * factor)**2
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
plt.title('2U en función de (r *B)^2 r = 0.035 m')
plt.grid(False)
plt.legend()
plt.show()
