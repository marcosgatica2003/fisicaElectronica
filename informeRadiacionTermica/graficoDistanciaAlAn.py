import matplotlib.pyplot as plt

distancias = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
radiacion = [0.182, 0.173, 0.159, 0.145, 0.132, 0.114, 0.1, 0.082, 0.068, 0.059, 0.05, 0.041, 0.036, 0.027, 0.027, 0.023, 0.018, 0.014, 0.009, 0.009, 0.009]

plt.figure()
plt.plot(distancias, radiacion, label='Aluminio anodizado', marker='o')

plt.title('')
plt.xlabel('Distancia (cm)', fontsize=30)
plt.ylabel('Radiación (mW)', fontsize=30)
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)

plt.legend()
plt.show()
