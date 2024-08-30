#escribe el siguiente codigo en el archivo visualizacionTitanic.py para importar las bibliotecas matploit, seaborn, y numpy
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#configurar el generador de numeros aleatorios
rng=np.random.RandomState(0)

#generar un rando de valores en el eje x
x= np.linspace(0,10,500)

#generar datos aleatorios y calcular la suma acumulada
y=np.cumsum(rng.randn(500,6),axis=0)

#graficar los datos
plt.plot(x,y)
plt.legend('ABCDEF', ncol=2, loc='upper left')
plt.show()

sns.set() #aplicar estilo de seaborn
plt.plot(x,y)
plt.legend('ABCDEF', ncol=2, loc='upper left')
plt.show()

y_val = x ** 2 
plt.scatter(x,y_val, marker='s', color='g')
plt.title('grafica de dispersión')
plt.xlabel('eje x')
plt.ylabel('eje y')
plt.show()
