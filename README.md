# Kmeans work 🛠️

Bienvenido a mi repositorio de Kmeans en Github! 🚀

_Aquí podrás encontrar el código que he utilizado para desarrollar una aplicación simple
en la que muestro distintos usos del algoritmo Kmeans._

_Dentro de la aplicación hay explicaciones 
de como funciona el algoritmo para ese caso específico, que hace y que datos utiliza._

### ¿Perooo, que es Kmeans?

- **_Kmeans_** o también conocido como **_Kmedias_** es un método de agrupamiento, que tiene como objetivo la partición de un conjunto de **n** observaciones 
en **k** grupos (_clusters_) en el que cada observación pertenece al grupo cuyo valor medio es más cercano.


- El problema es computacionalmente difícil [**(NP-hard)**](https://jcc.dcc.fceia.unr.edu.ar/2016/slides/2016-paredes-restrepo.pdf). Sin embargo, hay eficientes heurísticas que se emplean comúnmente y convergen rápidamente a un óptimo local. 
Estos suelen ser similares a los algoritmos esperanza-maximización de mezclas de distribuciones gausianas por medio de un enfoque de refinamiento iterativo empleado por ambos algoritmos.

- __NP__:
Son el conjunto de problemas que pueden ser resueltos en tiempo polinómico por una máquina de [Turing](https://formatalent.com/que-es-una-maquina-de-turing-y-como-funciona/) no determinista.


> _Si vas a usar muchos datos, intenta buscar variaciones del algoritmo mas avanzadas para ahorrar tiempo._



### El algoritmo en si es simple ⚙️:
Dado un conjunto de observaciones (x1, x2, …, xn), donde cada observación es un vector real de **d** dimensiones, **_kmeans_** construye una partición de las observaciones en **k** conjuntos (k ≤ n)
a fin de minimizar la suma de los cuadrados dentro de cada grupo 
**(WCSS): S = {S1, S2, …, Sk}**

<picture>
 <source media="(prefers-color-scheme: dark)" srcset="https://wikimedia.org/api/rest_v1/media/math/render/svg/5337aaa52e8956d39a6d4c0d9b022d26540b4a56">
 <source media="(prefers-color-scheme: light)" srcset="https://wikimedia.org/api/rest_v1/media/math/render/svg/5337aaa52e8956d39a6d4c0d9b022d26540b4a56">
 <img alt="YOUR-ALT-TEXT" src="https://wikimedia.org/api/rest_v1/media/math/render/svg/5337aaa52e8956d39a6d4c0d9b022d26540b4a56">
</picture>

donde **µ**<sub>i</sub> es la media de puntos en **S**<sub>i</sub>. 



## Datos del proyecto 📋

**_El código está completamento hecho en [Python](https://www.python.org/)._**

__Para desarrollar el programa usare las siguientes librerias 📖:__
-    [Numpy](https://numpy.org/)
-    [Scikit-learn](https://scikit-learn.org/stable/)
-    [Flet](https://flet.dev/)
> [!NOTE]
> Si no tienes los paquetes instalados o trabajas en un Entorno de Desarollo, los puedes instalar así con pip:

```
pip install numpy
```
```
pip install scikit-learn
```
```
pip install flet
```

## Muchas gracias por tomar el tiempo de leer esto 🎁
-    Comenta a otros sobre este proyecto 📢
-    Con ❤️ por [marcosplaza0](https://github.com/marcosplaza0)
