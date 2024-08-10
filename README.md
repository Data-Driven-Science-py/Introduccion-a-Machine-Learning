# Aprendizaje automatico
El aprendizaje automatico es un proceso de optimizacion matematica algoritmica que nos permite crear algoritmos que no dependan de instrucciones especificas para llegar a la conclusion deseada.

Es asi que todos los procesos pueden descritos en estos terminos a medida que puedan ser representados por ecuaciones que puedan ser optimizadas por medios computacionales. Entre estos medios computacionales, el mas importante del cual la mayor parte del area esta desarrollado, es el tal llamado **Descenso de Gradiente**.

# Descenso de Gradiente - Gradient Descent
Es el metodo computacional del cual se derivan diversas alternativas para el llamado **entrenamiento**(proceso de optimizacion) de la mayor parte de los modelos que existen hoy dia. Fue creado por el renombrado cientifico Cauchy(1847) y refinado por otros mas adelante, pero se enuncia de la siguiente manera:

#### Teorema 1: Descenso de Gradiente
Dada una aplicacion/funcion $f$ diferenciable y convexa en un dominio $X$, se cumple que la sucesion $a_n$ definida como sucesion de Cauchy en el dominio $X$ converge al minimo de $f$.

### $a_{n+1} = a_n - \gamma \nabla f(a_n)$

Basicamente aprovecha las propiedades de operadores matematicos para poder dar pasos hacia una solucion optimizada:

![image](https://raw.githubusercontent.com/Data-Driven-Science-py/Introduccion-a-Machine-Learning/main/src/image.webp)

# Funcion de costo
Es una medida que determina una relacion entre dos conjuntos de datos cuya resultante deberia de minimizarse, particularmente util con el descenso de gradiente dado su naturaleza numerica. Un ejemplo ampliamente utilizado es el error medio cuadratico:
### $\mathbb(E)[(\hat{O^t} - O^t)^2]$


