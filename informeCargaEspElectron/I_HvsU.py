import matplotlib.pyplot as plt

# Datos de la tabla de 5 cm

U_5 = [300, 280, 260.7, 240.8, 220.7, 200.2, 180.4, 160.8]
I_H_5 = [1.60, 1.55, 1.49, 1.44, 1.38, 1.319, 1.25, 1.17]

# Datos de la tabla de 4,5 cm

U_4_5 = [300, 280.6, 260, 240.2, 220.2, 200, 180, 160.2]
I_H_4_5 = [1.77, 1.69, 1.64, 1.58, 1.51, 1.44, 1.37, 1.27]

# Datos de la tabla de 4 cm

U_4 = [300.5, 280.3, 260.6, 240.1, 220.4, 200.1, 180.6, 160.1]
I_H_4 = [1.979, 1.92, 1.85, 1.769, 1.709, 1.61, 1.529, 1.44]

# Datos de la tabla de 3,5 cm

U_3_5 = [300.4, 280.5, 260, 240.3, 220.2, 200.1, 180.1, 160.3]
I_H_3_5 = [2.25, 2.179, 2.14, 2.03, 1.969, 1.859, 1.77, 1.65]

# Datos de la tabla de 3 cm

U_3 = [300.3, 280.2, 260, 240.5, 220.1, 200.2, 180, 160]
I_H_3 = [2.65, 2.56, 2.48, 2.38, 2.27, 2.18, 2.05, 1.95]

# Datos de la tabla de 2,5 cm

U_2_5 = [300, 280.6, 260.2, 240.5, 220.2, 200.2, 180.1, 160.3]
I_H_2_5 = [3.26, 3.13, 3.03, 2.87, 2.76, 2.56, 2.42, 2.33]

# Datos de la tabla de 2 cm

U_2 = [300.5, 280.2, 260, 240.1, 220.2, 200.5, 180.2, 160.3]
I_H_2 = [4.01, 3.88, 3.73, 3.60, 3.45, 3.31, 3.13, 2.92]


plt.figure()
plt.plot(U_5, I_H_5, label='5 cm', marker='o')
plt.plot(U_4_5, I_H_4_5, label='4.5 cm', marker='o')
plt.plot(U_4, I_H_4, label='4 cm', marker='o')
plt.plot(U_3_5, I_H_3_5, label='3.5 cm', marker='o')
plt.plot(U_3, I_H_3, label='3 cm', marker='o')
plt.plot(U_2_5, I_H_2_5, label='2.5 cm', marker='o')
plt.plot(U_2, I_H_2, label='2 cm', marker='o')

plt.title('')
plt.xlabel('U (V)', fontsize=15)
plt.ylabel('I_H (A)', fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.grid(False)

plt.legend()
plt.show()

