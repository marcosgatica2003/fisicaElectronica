import matplotlib.pyplot as plt

tempChapaNegra = [51, 50.4, 49.5, 48.8, 47.5, 46.6, 45.8, 45.1, 42.4, 41.5, 40.4, 39.4, 38.5, 37.9]
radChapaNegraPasco = [3.8, 3.6, 3.5, 3.3, 3.1, 3, 2.9, 2.7, 2.2, 2, 1.9, 1.7, 1.5, 1.4]

if len(tempChapaNegra) == len(radChapaNegraPasco):
    print("Bien chapa negra")

tempPlomo = [51, 50.5, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37]
radPlomoPasco = [3.5, 3.3, 3.2, 3, 2.9, 2.7, 2.5, 2.4, 2.2, 2, 1.9, 1.8, 1.6, 1.4, 1.3, 1.1]

if len(tempPlomo) == len(radPlomoPasco):
    print("Bien plomo")

tempAlAn = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40]
radAlAnPasco = [2.9, 2.7, 2.6, 2.4, 2.2, 2, 1.9, 1.8, 1.6, 1.5, 1.3]

if len(tempAlAn) == len (radAlAnPasco):
    print("Bien Aluminio An.")

tempCobre = [51.3, 51.5, 50.6, 49.6, 48.6, 47.1, 45.9, 44.7, 43.2, 40.7, 40.3, 38.8]
radCobrePasco = [1.7, 1.6, 1.5, 1.4, 1.3, 1.2, 1.1, 1, 0.9, 0.8, 0.7, 0.6]

if len(tempCobre) == len(radCobrePasco):
    print("Bien Cobre")

tempAluminio = [51.7, 50.8, 49.6, 48.6, 47.6, 46.6, 45.6, 44.6, 43.6, 42.6, 41.6, 40.6, 39.6, 38.6, 37.6, 36.4]
radAluminioPasco = [1.4, 1.4, 1.3, 1.3, 1.2, 1.1, 1, 1, 0.9, 0.8, 0.8, 0.7, 0.6, 0.6, 0.5, 0.4]

if len(tempAluminio) == len (radAluminioPasco):
    print("Bien Aluminio")


plt.figure()
plt.plot(tempAluminio, radAluminioPasco, label='Aluminio', marker='o')
plt.plot(tempPlomo, radPlomoPasco, label='Plomo', marker='o')
plt.plot(tempCobre, radCobrePasco, label='Cobre', marker='o')
plt.plot(tempAlAn, radAlAnPasco, label='Plomo', marker='o')
plt.plot(tempChapaNegra, radChapaNegraPasco, label='Cobre', marker='o')


plt.title('Tendencia de radiación en función de la tempratura')
plt.xlabel('Temperatura (ºC)')
plt.ylabel('Sensor Pasco (mV)')
plt.legend()
plt.show()
