import matplotlib.pyplot as plt
import pandas as pd

# Datos de ejemplo
data = {
    'Intensidad': [100, 80, 60, 40, 20],  
    'Energía': [302.5, 300, 278, 248, 198.5],
}

# Crear DataFrame
df = pd.DataFrame(data)

# Crear gráfico
plt.figure(figsize=(10, 6))
plt.plot(df['Intensidad'], df['Energía'], marker='o')


plt.title('Energía $V_{0}$ en función de la Intensidad')
plt.xlabel('Intensidad %')
plt.ylabel('Energía $V_{0}$ (mV)')
plt.grid(True)

# Invertir el eje x
plt.gca().invert_xaxis()

# Mostrar el gráfico
plt.show()